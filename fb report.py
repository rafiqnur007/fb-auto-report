from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Setup Chrome options
chrome_options = Options()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

# Initialize WebDriver (Use appropriate chromedriver path if needed)
service = Service("chromedriver.exe")  # Change path if necessary
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open Facebook login page
driver.get("https://www.facebook.com/")
wait = WebDriverWait(driver, 10)

# Login process
email = "9898989898"  # Replace with actual email/phone
password = "pass123$%"  # Replace with actual password

wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
wait.until(EC.presence_of_element_located((By.ID, "pass"))).send_keys(password)
wait.until(EC.element_to_be_clickable((By.NAME, "login"))).click()

# Wait for login to complete
time.sleep(5)  # This can be improved with better wait conditions

# Navigate to target profile (Change the profile URL)
profile_url = "https://www.facebook.com/profile.php?id=100089108025261"
driver.get(profile_url)

# Wait for the page to load
time.sleep(4)

# Click on the three-dot menu
wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="More"]'))).click()
time.sleep(3)

# Click on "Find or Report Profile"
wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Find or report profile")]'))).click()
time.sleep(3)

# Select "Report Profile"
wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Report")]'))).click()
time.sleep(3)

# Choose "Pretending to be me"
wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Pretending to be me")]'))).click()
time.sleep(3)

# Submit the report
wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"Submit")]'))).click()
time.sleep(3)

# Click next button
wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"Next")]'))).click()
time.sleep(3)

# Click Done
wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"Done")]'))).click()

# Wait before closing
time.sleep(10)
driver.quit()
