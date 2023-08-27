import re
from playwright.sync_api import Page, expect

def testLogin(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.screenshot(path="demo.png")

    expect(page).to_have_title(re.compile("Swag Labs"))

    # create a locator
    get_started = page.get_by_role("link", name="Get started")

    # Expect an attribute "to be strictly equal" to the value.
    expect(get_started).to_have_attribute("href", "/docs/intro")

    # Click the get started link.
    get_started.click()

    # Expects the URL to contain intro.
    expect(page).to_have_url(re.compile(".*intro"))