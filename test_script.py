import time
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction


def test_demo_chrome():
    desired_cap = {}
    desired_cap['deviceName'] = 'Nexus 5'
    desired_cap['platformName'] = 'Android'
    desired_cap['platformVersion'] = '10.0'
    desired_cap['browserName'] = 'Chrome'
    desired_cap['chromedriverExecutableDir'] = 'C:\\WebDriver'  # TODO: Change this to relative path
    try:
        appium_service = AppiumService()
        appium_service.start()
        print(appium_service.is_running)
        print(appium_service.is_listening)
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_cap)
        driver.get("https://www.facebook.com")

        # driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'SomeAccessibilityID')
        # element = "xpath_element"
        # action = TouchAction(driver)
        # action.tap(element).perform()
        # action.press(element).wait(3000).move_to(element).perform().release()
        # action.long_press(element,duration=3).perform()
        # contexts = driver.contexts
        # driver.switch_to.context('WEBVIEW_Chrome')
        # driver.start_activity(app_package='app_package', app_activity='app_Activity')

        print(driver.title)
        driver.press_keycode(10)
        time.sleep(3)
        driver.quit()
    except:
        print("Exception occurred.")
    finally:
        appium_service.stop()
        print(appium_service.is_listening)
        print(appium_service.is_running)
