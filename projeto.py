from typing import Text
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import getpass
import random
from PySimpleGUI import PySimpleGUI as sg
 
class BotDeComents:
    def __init__(self, user, password, comentario, link, vezes,):
        self.user = user
        self.password = password
        self.comentario = comentario
        self.link = link
        self.vezes = vezes
        self.driver = webdriver.Chrome()
        
    
    def login(self):
        self.driver.get('https://www.instagram.com')
        print ('\n'* 130)
        print ("Fazendo login, aguarde... \n Isso pode demorar um pouco.")
        time.sleep(3)
        campo_user = self.driver.find_element_by_xpath ('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[1]/div/label/input')
        campo_user.send_keys(self.user)
        campo_senha = self.driver.find_element_by_xpath ('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[2]/div/label/input')
        campo_senha.send_keys(self.password, Keys.ENTER)
        time.sleep(5)
        print ('\n'* 130)
        print ("Login feito com sucesso.")
        salvar_senha = self.driver.find_element_by_xpath ('/html/body/div[1]/section/main/div/div/div/section/div/button')
        salvar_senha.send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.get(self.link)
                
    def sorteio(self):
        time.sleep(3)
        curtir = self.driver.find_element_by_xpath ('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button')
        curtir.click()
        time.sleep(3)
        ('\n'* 130)
        for c in range (self.vezes):
            comentar = self.driver.find_element_by_class_name ('Ypffh')
            comentar.click()
            comentar1 = self.driver.find_element_by_class_name ('Ypffh')
            comentar1.send_keys (self.comentario, Keys.ENTER)
            comentando_igual_a_gente()
            print ("Comentario feito.")
        print ('Foram feitos {} comentarios com exito.'.format(self.vezes))

        
def comentando_igual_a_gente():
    rand = random.randint(1,5)
    time.sleep(rand)

tema = {'BACKGROUND': '#1a1918',
                    'TEXT': '#ffffff',
                    'INPUT': '#ffffff',
                    'TEXT_INPUT': '#000000',
                    'SCROLL': '#c7e78b',
                    'BUTTON': ('black', '#ffffff'),
                    'PROGRESS': ('#01826B', '#D0D0D0'),
                    'BORDER': 3,
                    'SLIDER_DEPTH': 3,
                    'PROGRESS_DEPTH': 0}

sg.theme_add_new('tema', tema)

sg.theme('tema')

layout = [
        [sg.Text('INSTA BOT', size=(25,1), font="Courier 30")],
        [sg.Text('Versão 0.1 (Beta)  By: @ucarlux', size=(50,1), font="Courier 10")], 
        [sg.Text('Usuario:', size=(18,1)), sg.Input(key= 'user', size=(12,1))],
        [sg.Text('Senha:', size=(18,1)), sg.Input(key= 'senha',password_char="*", size=(12,1))],
        [sg.Text('Link:', size=(18,1)), sg.Input(key= 'link', size=(40,1))],
        [sg.Text('Número de Comentarios:', size=(18,1)), sg.Input(key= 'vzs', size=(12,1))],
        [sg.Text('Comentarios:', size=(18,1)), sg.Input(key= 'comentario', size=(12,1))],
        [sg.Button('Iniciar')],
        [sg.Output(size=(30,3))]
            ]

janela = sg.Window('Instagram Bot', layout, icon='instagram.ico', no_titlebar=False, alpha_channel=10, grab_anywhere=True)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Iniciar':
        if valores['user'] == '' or valores['senha'] == '' or valores['link'] == '' or valores['vzs'] == '' or valores['comentario'] == '':
            sg.Popup('Há campos vazios a serem preenchidos', title='Atenção')
        else:
            vzs1 = valores['vzs']
            vzs2 = int(vzs1)
            Bot = BotDeComents(valores['user'], valores['senha'], valores['comentario'], valores['link'], vzs2)
            try:
                Bot.login()
            except:
                print ('Ocorreu um erro com seu login altere as credenciais')
                Bot.login()
            Bot.sorteio()
    