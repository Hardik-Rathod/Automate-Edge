from selenium.webdriver import Edge
import time
from selenium.webdriver.common.by import By

# Create a new instance of the Edge browser
browser = Edge()

# Loop through the numbers 1-100 and search for each one
for i in range(1, 46):
    # Construct the search URL
    search_url = f'https://www.bing.com/search?q={i}'

    # Navigate to the search URL
    browser.get(search_url)

    # Wait for the page to load
#    time.sleep(2)

    # Get the search results and print them to the console
    search_results = browser.find_elements(By.XPATH, '//li[@class="b_algo"]')
#    for result in search_results:
#        print(result.text)

# Close the browser
browser.quit()
