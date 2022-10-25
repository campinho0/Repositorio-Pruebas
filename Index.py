import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options



class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        firefox_options = Firefox_Options()
        firefox_options.binary = "C:/Program Files/Mozilla Firefox/firefox.exe"
        self.driver = webdriver.Firefox(executable_path="C:/firefox_webdriver/geckodriver.exe")


    
    def test_overload_register(self):
        driver = self.driver
        driver.get("https://parabank.parasoft.com/parabank/index.htm")
        for i in range(50):
            try:
                time.sleep(7) #Tiempo de espera entre registros
                print("-------------", i, "-------------")
                driver.find_element(By.LINK_TEXT, 'Register').click()
                driver.find_element(By.XPATH, '//input[@id="customer.firstName"]').send_keys("registro ")
                driver.find_element(By.XPATH, '//input[@id="customer.lastName"]').send_keys(i)
                driver.find_element(By.XPATH, '//input[@id="customer.address.street"]').send_keys("Calle", i)
                driver.find_element(By.XPATH, '//input[@id="customer.address.city"]').send_keys("Ciudad", i)
                driver.find_element(By.XPATH, '//input[@id="customer.address.state"]').send_keys("Estado", i)
                driver.find_element(By.XPATH, '//input[@id="customer.address.zipCode"]').send_keys("52430", i)
                driver.find_element(By.XPATH, '//input[@id="customer.phoneNumber"]').send_keys("123456", i)
                driver.find_element(By.XPATH, '//input[@id="customer.ssn"]').send_keys("098765", i)
                #Cambiar el nombre de usuario en cada registro si se quieren registrar correctamente
                driver.find_element(By.XPATH, '//input[@id="customer.username"]').send_keys("ususr_d_877ñ_" , i)
                driver.find_element(By.XPATH, '//input[@id="customer.password"]').send_keys("contrasena", i)
                driver.find_element(By.XPATH, '//input[@id="repeatedPassword"]').send_keys("contrasena", i)
                driver.find_element(By.XPATH, '//input[@value="Register"]').click()
                
                try:
                    user_name = driver.find_element(By.XPATH, '//p[@class="smallText"]')
                    print(user_name.text)
                    driver.find_element(By.XPATH, "html/body/div/div[3]/div/ul/li[8]").click()
                except:
                    print("No se registro usuario")
                    time.sleep(2)
                    driver.get("https://parabank.parasoft.com/parabank/index.htm")
                finally:
                    driver.get("https://parabank.parasoft.com/parabank/index.htm")
            except:
                time.sleep(5)
                driver.refresh()
                print("------------------------------\n Sobrecarga en el servidor \n------------------------------")
                driver.find_element(By.XPATH, "html/body/div/div[3]/div/ul/li[8]").click()
    
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__" :
    unittest.main()

