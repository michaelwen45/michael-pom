# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


class WebView(object):

    def __init__(self, base_url, selenium, timeout=10, **kwargs):
        self.base_url = base_url
        self.timeout = timeout
        self.selenium = selenium
        self.wait = WebDriverWait(self.selenium, self.timeout)
        self.kwargs = kwargs

    @property
    def _root(self):
        return self.selenium

    def find_element(self, locator):
        return self._root.find_element(*locator)

    def find_elements(self, locator):
        return self._root.find_elements(*locator)

    def is_element_present(self, locator):
        try:
            return self.find_element(locator)
        except NoSuchElementException:
            return False

    def is_element_displayed(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except NoSuchElementException:
            return False

    def scroll_element_into_view(self, locator, x=0, y=0):
        el = self.find_element(locator)
        self.selenium.execute_script(
            'arguments[0].scrollIntoView();'
            'window.scrollBy(arguments[1], arguments[2]);', el, x, y)
        return el
