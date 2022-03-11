from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, '.form-control[name="login-username"]')
    REG_FORM_LINK = (By.CSS_SELECTOR, '.form-control[name="registration-email"]')
