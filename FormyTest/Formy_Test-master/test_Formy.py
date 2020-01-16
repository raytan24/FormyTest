from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  
import pytest


@pytest.fixture()
def driver():
    my_options = Options()  
    #options.add_argument("--headless") 
    my_options.headless = True
    driver = webdriver.Chrome(options=my_options)      
    yield driver
    driver.quit()
    # create a object for the chrome driver and pass around

def test_formy_form(driver):
    driver.get("https://formy-project.herokuapp.com/buttons")
   # assert "Formy" in driver.title
    driver.save_screenshot("Main.png")
    
def test_formy_primary_buttons(driver):
    driver.get("https://formy-project.herokuapp.com/buttons")
    elem = driver.find_element_by_css_selector('.btn-primary')
    driver.save_screenshot("Screeny1.png")
    assert "Primary" == elem.text
    
def test_formy_success_buttons(driver):
    driver.get("https://formy-project.herokuapp.com/buttons")
    elem = driver.find_element_by_css_selector('.btn-success')
    #assert "Success" == elem.text

def test_formy_info_buttons(driver):
    driver.get("https://formy-project.herokuapp.com/buttons")
    elem = driver.find_element_by_css_selector('.btn-info')
    assert "Info" == elem.text
   
def test_formy_warning_buttons(driver):
    driver.get("https://formy-project.herokuapp.com/buttons")
    elem = driver.find_element_by_css_selector('.btn-warning')
    assert "Warning" == elem.text
    
def test_formy_danger_buttons(driver):
    driver.get("https://formy-project.herokuapp.com/buttons")
    elem = driver.find_element_by_css_selector('.btn-danger')
    assert "Danger" == elem.text
    
def test_formy_link_buttons(driver):
    driver.get("https://formy-project.herokuapp.com/buttons")
    elem = driver.find_element_by_css_selector('.btn-link')
    assert "Link" == elem.text
    
def test_formy_left_buttons(driver):
    driver.get("https://formy-project.herokuapp.com/buttons")
    elem = driver.find_element_by_xpath('//button[text()="Left"]')
    assert "Left" == elem.text
    
def test_formy_middle_buttons(driver):
    driver.get("https://formy-project.herokuapp.com/buttons")
    elem = driver.find_element_by_xpath('//button[text()="Middle"]')
    assert "Middle" == elem.text
    
def test_formy_right_buttons(driver):
    driver.get("https://formy-project.herokuapp.com/buttons")
    elem = driver.find_element_by_xpath('//button[text()="Right"]')
    assert "Right" == elem.text

def test_formy_1_buttons(driver):
    driver.get("https://formy-project.herokuapp.com/buttons")
    elem = driver.find_element_by_xpath('//button[text()="1"]')
    assert "1" == elem.text

def test_formy_2_buttons(driver):
    driver.get("https://formy-project.herokuapp.com/buttons")
    elem = driver.find_element_by_xpath('//button[text()="2"]')
    assert "2" == elem.text

def test_formy_dropdown_buttons(driver):
    driver.get("https://formy-project.herokuapp.com/buttons")
    elem = driver.find_element_by_id('btnGroupDrop1')
    assert "Dropdown" == elem.text

