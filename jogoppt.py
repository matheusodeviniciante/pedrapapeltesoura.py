'''6. Jogo de Pedra, Papel e Tesoura
Descrição: Implemente o clássico jogo de Pedra, Papel e Tesoura, onde o usuário joga contra o computador.
O programa deve anunciar o vencedor a cada rodada e permitir múltiplas jogadas.
Conceitos Praticados: Condicionais, laços de repetição, geração de números aleatórios.'''
from random import randint
import os
import time

cond = True
usuarioP = 0
Computadorp = 0
pontoMAX = int(input('Defina a Pontuação Maxima para Ganhar'))
pontoVALOR = int(input('Escolha quantos Pontos Vale cada Rodada'))


while cond:
    print(f'Pontos Computador: {Computadorp} || Pontos Usuario: {usuarioP}\n')
    usuario = input('escolha Papel, Pedra Ou Tesoura ')
    computador = randint(1,3)
    if computador == 1:
        computador = 'papel'
    if computador == 2:
        computador = 'pedra'
    if computador == 3:
        computador = 'tesoura'

    if usuario == 'tesoura' and computador == 'papel':
        os.system('cls')
        print(f'Pontos Computador: {Computadorp} || Pontos Usuario: {usuarioP}\n')
        print(f'\nUsuario Ganhou !! escolheu: {usuario.upper()} e o computador escolheu: {computador.upper()}\n')
        time.sleep(2)
        os.system('cls')
        usuarioP += pontoVALOR

    if usuario == 'pedra' and computador == 'papel':
        os.system('cls')
        print(f'Pontos Computador: {Computadorp} || Pontos Usuario: {usuarioP}\n')
        print(f'\nO Computador Ganhou!! escolheu: {usuario.upper()} e o computador escolheu: {computador.upper()}\n')
        time.sleep(2)
        os.system('cls')
        Computadorp += pontoVALOR

    if usuario == 'papel' and computador == 'papel':
        os.system('cls')
        print('\nTeve Um impate\n')
        time.sleep(2)
        os.system('cls')

    if usuario == 'tesoura' and computador == 'tesoura':
        os.system('cls')
        print('\nTeve Um impate\n')
        time.sleep(2)
        os.system('cls')

    if usuario == 'pedra' and computador == 'tesoura':
        os.system('cls')
        print(f'Pontos Computador: {Computadorp} || Pontos Usuario: {usuarioP}\n')
        print(f'\n Usuario Ganhou!! escolheu: {usuario.upper()} e o computador escolheu: {computador.upper()}\n')
        time.sleep(2)
        os.system('cls')
        usuarioP += pontoVALOR
        
    if usuario == 'papel' and computador == 'tesoura':
        os.system('cls')
        print(f'Pontos Computador: {Computadorp} || Pontos Usuario: {usuarioP}\n')
        print(f'\nComputador Ganhou !! escolheu: {usuario.upper()} e o computador escolheu: {computador.upper()}\n')
        time.sleep(2)
        os.system('cls')
        Computadorp += pontoVALOR

    if usuario == 'tesoura' and computador == 'pedra':
        os.system('cls')
        print(f'Pontos Computador: {Computadorp} || Pontos Usuario: {usuarioP}\n')
        print(f'\no Computador Ganhou !! escolheu: {usuario.upper()} e o computador escolheu: {computador.upper()}\n')
        time.sleep(2)
        os.system('cls')
        Computadorp += pontoVALOR

    if usuario == 'pedra' and computador == 'pedra':
        os.system('cls')
        print('\nTeve um Impate\n')
        time.sleep(2)
        os.system('cls')
        
    if usuario == 'papel' and computador == 'pedra':
        os.system('cls')
        print(f'Pontos Computador: {Computadorp} || Pontos Usuario: {usuarioP}\n')
        print(f'\nO usuario Ganhou !! escolheu: {usuario.upper()} e o computador escolheu: {computador.upper()}\n')
        time.sleep(2)
        os.system('cls')
        usuarioP += 10
        

    if usuarioP == pontoMAX or Computadorp == pontoMAX:
        print(f'Pontos Computador: {Computadorp} || Pontos Usuario: {usuarioP}\n')
        cond = False




if usuarioP == pontoMAX:
    print("Usuario GANHOU A COMPETIÇÃO")
else:
    print("O computador GANHOU A COMPETIÇÃO")
    
    
        
    
    
  
    

    
