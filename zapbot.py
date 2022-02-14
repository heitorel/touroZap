from selenium import webdriver
import time
import pandas as pd

class zapbot:
 
    def __init__(self):
        googleSheetId = 'teco da url'
        worksheetName = 'nome'
        url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(googleSheetId,worksheetName)   
        planilha_alunos = pd.read_csv(url) 
        self.pessoas = planilha_alunos["Pessoa"]
        self.numeros = planilha_alunos["Numero"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br') 
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)
 
    def EnviarMensagens(self):
        i=0
        for pessoa in self.pessoas:
            numero = str(self.numeros[i])
            print(numero)
            self.driver.get('https://web.whatsapp.com/send?phone='+numero+'&amp;text&amp;app_absent=0')
            time.sleep(20)
            self.mensagem = "Oieee "+pessoa+". Tudo bem??"
            chat_box = self.driver.find_element_by_class_name('p3_M1')
            time.sleep(10)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(10)
            botao_enviar.click()
            time.sleep(10)
            i=i+1

bot = zapbot()
bot.EnviarMensagens()