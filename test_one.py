import pytest

url = "https://plugins.jenkins.io/shiningpanda/"


def test_smoke_one(driver):
    driver.get(url)
    page_header = driver.find_element_by_css_selector(".title-wrapper .title").text

    assert page_header == "ShiningPanda"
