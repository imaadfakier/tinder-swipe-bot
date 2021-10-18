import config
from selenium import webdriver
import time
import os
# import ait
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

CHROME_DRIVER_PATH = 'type chrome driver path here'


def wait(seconds):
    time.sleep(seconds)


driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(url='https://tinder.com/')
driver.maximize_window()

# TODO 1: log into tinder [DONE]
wait(1)
log_in_button = driver.find_element_by_xpath(
    xpath='//*[@id="q-2110398392"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a'
)
log_in_button.click()

# # --- gmail sign in: not possible
# wait(3)
# google_sign_in = driver.find_element_by_xpath(
#     xpath='//*[@id="q456187828"]/div/div/div[1]/div/div[3]/span/div[1]/div/button'
#     # xpath='/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[1]/div/button'
# )
# google_sign_in.click()
# wait(5)
# # gmail_username_input = driver.find_element_by_xpath(
# #     # xpath='//*[@id="identifierId"]'
# #     xpath='/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]'
# #           '/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'
# # )
# # gmail_username_input.send_keys(os.environ.get('TINDER_GMAIL_USERNAME'))
# ait.write('{username}'.format(username=os.environ.get('TINDER_GMAIL_USERNAME')))
# ait.click()
# # time.sleep(7)
# # ait.write(f'{os.environ.get("TINDER_GMAIL_PASSWORD")}')
#
# # --- phone number authentication: not possible due to robot test
# # ...
#
# facebook sign in
wait(3)
facebook_log_in = driver.find_element_by_xpath(
    xpath='//*[@id="q456187828"]/div/div/div[1]/div/div[3]/span/div[2]/button'
)
facebook_log_in.click()
wait(5)
# print(driver.window_handles)  # list is returned
tinder_window = driver.window_handles[0]
facebook_login_window = driver.window_handles[1]
driver.switch_to.window(facebook_login_window)
# print(driver.title)
facebook_email_input = driver.find_element_by_name(name='email')
facebook_email_input.send_keys(os.environ.get('TINDER_FACEBOOK_EMAIL'))
facebook_password_input = driver.find_element_by_name(name='pass')
facebook_password_input.send_keys(os.environ.get('TINDER_FACEBOOK_PASSWORD'))
facebook_log_in_button = driver.find_element_by_id(id_='loginbutton')
facebook_log_in_button.click()
driver.switch_to.window(tinder_window)

# TODO 2: dismiss all requests [DONE]
wait(10)
html_elements_x_path = [
    '//*[@id="q456187828"]/div/div/div/div/div[3]/button[1]',
    '//*[@id="q456187828"]/div/div/div/div/div[3]/button[2]',
    '//*[@id="q-2110398392"]/div/div[2]/div/div/div[1]/button'
]
for html_element_x_path in html_elements_x_path:
    html_tag = driver.find_element_by_xpath(xpath=html_element_x_path)
    html_tag.click()

# TODO 3: swipe left/right on every person [DONE]
wait(10)
swipe_right_button = driver.find_element_by_xpath(
    xpath='//*[@id="q-2110398392"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button'
)
for _ in range(100):
    try:
        swipe_right_button.click()
        # wait(1)
    except NoSuchElementException:
        pass
    except ElementClickInterceptedException as e:
        try:
            disallow_add_to_home_screen = driver.find_element_by_xpath(
                xpath='//*[@id="q456187828"]/div/div/div[2]/button[2]'
            )
            disallow_add_to_home_screen.click()
        except NoSuchElementException as e:
            back_to_tinder = driver.find_element_by_css_selector('.itsAMatch a')
            back_to_tinder.click()
    finally:
        wait(3)

# TODO 4: log out after 100 swipes
# ...

# driver.quit()
