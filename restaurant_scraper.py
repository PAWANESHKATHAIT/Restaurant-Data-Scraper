from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Ensure you have the appropriate driver installed
url = "https://www.google.com/search?sca_esv=187175ea13837ba9&rlz=1C1OPNX_enIN1122IN1122&tbm=lcl&sxsrf=ADLYWIKG83gKNxPSXfWg_Xtk44SDpppn3Q:1734604723091&q=restaurant+in+india+with+phone+number&rflfq=1&num=10&sa=X&ved=2ahUKEwjAv-GS0rOKAxUH4jgGHcBqN30QjGp6BAgiEAE&biw=1280&bih=585&dpr=1.5#rlfi=hd:;si:;mv:[[28.710228800000003,77.438711],[28.558968399999998,77.15871729999999]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u5!2m2!5m1!1sgcid_3north_1indian_1restaurant!1m4!1u5!2m2!5m1!1sgcid_3chinese_1restaurant!1m4!1u2!2m2!3m1!1e1!1m4!1u1!2m2!1m1!1e1!1m4!1u1!2m2!1m1!1e2!2m1!1e2!2m1!1e5!2m1!1e1!2m1!1e3!3sIAEqAklO,lf:1,lf_ui:9"

try:
    # Open the webpage
    driver.get(url)
    time.sleep(5)  # Wait for the page to fully load

    # Extract restaurant details
    names = driver.find_elements(By.CSS_SELECTOR, 'span.OSrXXb')  # For restaurant names
    reviews = driver.find_elements(By.CSS_SELECTOR, 'span.yi40Hd.YrbPuc')  # For reviews
    locations = driver.find_elements(By.XPATH,
                                     '//div[contains(text(), "Noida") or contains(text(), "Uttar Pradesh")]')  # For locations
    phone_numbers = driver.find_elements(By.XPATH,
                                         '//div[contains(text(), "0") or contains(text(), "+91")]')  # For phone numbers

    # Prepare data
    restaurant_data = []
    for name, review, location, phone in zip(names, reviews, locations, phone_numbers):
        # Extract text or set to a default message if not found
        name_text = name.text.strip() if name.text else "Name not found"
        review_text = review.text.strip() if review.text else "Review not found"
        location_text = location.text.strip() if location.text else "Location not found"
        phone_text = phone.text.strip() if phone.text else "Phone not found"

        # Append the data in list format
        restaurant_data.append([name_text, review_text, location_text, phone_text])

    # Save to CSV
    with open('restaurant_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Review', 'Location', 'Phone Number'])  # Write headers
        writer.writerows(restaurant_data)  # Write data

    print("Data saved to 'restaurant_data.csv' successfully.")

finally:
    driver.quit()  # Close the browser
