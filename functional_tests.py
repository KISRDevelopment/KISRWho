from selenium import webdriver

import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_register(self):
        # Dr. Bu Sale7 has heard about a cool new KISR website that helps you find projects and fellow reserchers
        #  He checks out its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header say 'KISRWho'
        self.assertIn('KISRWho', self.browser.title)
        self.fail('Finish the tests!')

        # He sees a register button on the Navbar

        # When he clicks it, it takes him to a registration form asking for his Name, Email, Username and Password

        # He fills it out with his details

        # When he hits enter, the register button goes away and is replaced by his username and a logout button

        # He's also been redirected to his own profile page

if __name__ == '__main__':
    unittest.main(warnings='ignore')
