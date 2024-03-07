#esse programa retira as informações de uma tabela e cadastra em um sistema

import subprocess

import pyautogui
pyautogui.PAUSE = 0.5
import time

#entrar no navegador
pyautogui.click(x=1429, y=1057)

time.sleep(3)

#entrar no link
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press ('enter')
time.sleep(3)

#login

pyautogui.click(x=849, y=646)
pyautogui.write('camillysantiiago03@gmail.com')
time.sleep(3)

pyautogui.press('tab')
pyautogui.write('dayrol123')
pyautogui.click(x=942, y=859)
pyautogui.press('tab')
time.sleep(1)
#3 importar a base de dados

import pandas
tabela = pandas.read_csv('produtos.csv')

for linha in tabela.index:

    pyautogui.click(x=683, y=509)
    #codigo
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')

    #marca

    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')

    #tipo

    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')

    #categoria

    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    #preço
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    #custo
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    #observação
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter')
    pyautogui.scroll(5000)




