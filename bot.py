from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime

data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')


comments = ['comentario teste']



comentario = random.choice(comments)







class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver =  webdriver.Chrome(executable_path="local onde está o chromedriver_win32\chromedriver.exe")
    
    

    def login(self):

        chrome_options = Options()
        chrome_options.add_argument("--headless")

        chrome_driver = os.getcwd() +"\\chromedriver.exe"
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="local onde está o chromedriver_win32\chromedriver.exe")
        driver.get("https://www.instagram.com/")

        print('\n')
        print("Você realizou acesso ao Instagram")
        print('\n')
        time.sleep(5)
        try:
            login_button = driver.find_element_by_xpath(
                "//a[@href='/accounts/login/?source=auth_switcher']"
            )
            login_button.click()
        except:
            print('Você na página de login')
            pass
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)

        print("Você realizou o login no Instagram")
        print("Entrando no link do sorteio...")
        time.sleep(5)
        driver.get('link do sorteio')
        time.sleep(5)
        commentArea = driver.find_element_by_class_name('Ypffh')
        commentArea.click()
        time.sleep(5)
        comment = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').send_keys(comentario)
        print('\nVocê vai comentar:', comentario)
        time.sleep(8)
        publicar = driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
        print('Comentario 1/1 realizado com sucesso!')
        time.sleep(8)    
        print('\nTodos os comentarios foram enviados!! :) ')
        time.sleep(1)
        print('\nA ultima execução realizou as:',data_e_hora_em_texto)
        time.sleep(8)
        self.driver.close()
        time.sleep(1) 
        self.driver.quit()

        


bot = InstagramBot('seu usuario', 'senha')
bot.login()
