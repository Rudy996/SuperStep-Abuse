import re
from multiprocessing import Pool
from random import choice

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import requests
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-gpu')
options.add_argument('--disable-infobars')
options.add_argument("--mute-audio")
options.add_argument("--disable-blink-features")
options.add_argument('--profile-directory=Default')
options.add_argument("--mute-audio")
options.add_extension("2Captcha.crx")


acc = 3 #Сколько акков зарегать
o = ("1")
mail42 = o * acc
api = ("a4f4a87c814707ae0d945fbed367fa43") #Сюда ApiKey с RuCaptcha




def work(mail43):
    try:
        driver = webdriver.Chrome(executable_path=r"chromedriver\chromedriver.exe", options=options)
        wait = WebDriverWait(driver, 30)
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="apiKey"]'))).send_keys(api)
        driver.find_element_by_id("autoSubmitForms").click()
        driver.find_element_by_id("autoSolveRecaptchaV2").click()
        driver.find_element_by_id("autoSolveInvisibleRecaptchaV2").click()
        driver.find_element_by_id("autoSolveRecaptchaV3").click()
        driver.find_element_by_id("connect").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        driver.get("https://www.superstep.io/airdrop?ref=d0o6bp") # Реф.ссылка
        mail = "".join([choice("abcdefghijklmnopqrstuvwxyz013456789") for _ in range(15)]) + ("@gmail.com")
        password = "".join([choice("abcdefghijklmnopqrstuvwxyz013456789") for _ in range(15)])
        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="email"]'))).send_keys(mail)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="password"]'))).send_keys(password)
        time.sleep(20)
        g = 0
        h = 0
        j = 0
        while g == 0:
            if h != 60:
                if j != 10:
                    try:
                        driver.find_element_by_class_name("claim").click()
                        time.sleep(1)
                        h = h + 1
                        print(h)
                    except:
                        try:
                            driver.find_elements_by_class_name('mt16')
                            driver.find_element_by_class_name("ok").click()
                            # wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ok'))).click()
                            print("я хуесос")
                            time.sleep(1)
                            g = 1
                        except:
                            g = 0
                            j = j + 1
                            print("j: ", j)
                elif j == 10:
                    try:
                        driver.refresh()
                        mail = "".join([choice("abcdefghijklmnopqrstuvwxyz013456789") for _ in range(15)]) + (
                            "@gmail.com")
                        password = "".join([choice("abcdefghijklmnopqrstuvwxyz013456789") for _ in range(15)])
                        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="email"]'))).send_keys(mail)
                        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="password"]'))).send_keys(
                            password)
                        time.sleep(20)
                    except:
                        print("Капча уебанксая")
                    j = 0

            elif h == 60:
                try:
                    driver.refresh()
                    mail = "".join([choice("abcdefghijklmnopqrstuvwxyz013456789") for _ in range(15)]) + (
                        "@gmail.com")
                    password = "".join([choice("abcdefghijklmnopqrstuvwxyz013456789") for _ in range(15)])
                    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="email"]'))).send_keys(mail)
                    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="password"]'))).send_keys(
                        password)
                    time.sleep(20)
                except:
                    print("Капча не решилась")
                h = 0















    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    p = Pool(processes=5) #Кол-во потоков
    p.map(work, mail42)
