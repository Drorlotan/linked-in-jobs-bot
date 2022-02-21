from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = "C:/Users/drorlotan/PycharmProjects/development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(
    "https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&f_TPR=r604800&geoId=101620260&keywords=python%20developer&location=Israel")
time.sleep(3)
sign_in = driver.find_element(By.XPATH, "/html/body/div[3]/a[1]")
sign_in.click()
time.sleep(1)
email = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[1]/input")
email.send_keys("dragondror@gmail.com")
password = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[2]/input")
password.send_keys("#########")
sign_in_button = driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button")
sign_in_button.click()
time.sleep(3)

jobs_containers = driver.find_elements(By.CLASS_NAME,
                                       "job-card-container--clickable")

time.sleep(1)
job_number = 0
job_curr = 0


def applaying(requests):
    global job_curr
    try:
        submit_application = driver.find_element(By.LINK_TEXT, "Submit application")
        submit_application.click()
        time.sleep(1)
        exit_job = driver.find_element(By.CSS_SELECTOR, "cancel-icon")
        exit_job.click()
        time.sleep(2)
        requests += 1
        jobs_containers_click(jobs_containers, requests)
    except NoSuchElementException:
        for i in range(5):
            try:
                next_bottom = driver.find_element(By.CSS_SELECTOR,
                                                  '.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
                next_bottom.click()
            except NoSuchElementException:
                review_bottom = driver.find_element(By.XPATH,
                                                    "/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button[2]")
                review_bottom.click()
                submit_application = driver.find_element(By.LINK_TEXT, "Submit application")
                submit_application.click()
                time.sleep(1)
                exit_job = driver.find_element(By.CSS_SELECTOR, "cancel-icon")
                exit_job.click()
                time.sleep(2)
                requests += 1
                jobs_containers_click(jobs_containers, requests)
                break


def jobs_containers_click(jobs, requests):
    global job_curr
    print(requests)
    print(f"job_cuur = {job_curr}")
    jobs[requests].click()
    try:
        time.sleep(2)
        easy_apply = driver.find_element(By.CLASS_NAME, "jobs-apply-button--top-card")
        easy_apply.click()
        applaying(requests)
        time.sleep(1)
        requests += 1
        jobs_containers_click(jobs, requests)
    except NoSuchElementException:
        time.sleep(1)
        requests += 1
        jobs_containers_click(jobs, requests)


jobs_containers_click(jobs_containers, job_curr)
