import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_presence_of_basket_button(browser):
    browser.get(link)
    time.sleep(10)

    basket_button = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))

    assert basket_button > 0, "Basket button is not found"
