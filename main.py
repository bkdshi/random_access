from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
from datetime import datetime
import sys
import urllib.parse

domain = sys.argv[1]
urls = []

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument(f"--user-agent={user_agent}")

driver = webdriver.Chrome(options=options)
driver.get(urllib.parse.urljoin(domain, "sitemap.xml"))

time.sleep(1)

spans = driver.find_elements(By.TAG_NAME, "span")
for span in spans:
    text = span.text
    if text.find(urllib.parse.urljoin(domain, "posts")) != -1:
        urls.append(text)


path = random.choice(urls)
driver.get(path)

time.sleep(5)
print(datetime.now(), driver.title)
