import random

def jogar():

    print('**********************************')
    print('Bem vindo no jogo de Adinhinhação!')
    print('**********************************')

    numero_secreto = random.randrange(1,51,1)
    total_de_tentativas = 0
    pontuacao = 1000
    pontos_perdidos = 0
    print('Qual o nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Dificil')

    nivel = int(input('Define o nível: '))
    if(nivel == 1):
        total_de_tentativas = 10
    elif(nivel == 2):
        total_de_tentativas = 6
    else:
        total_de_tentativas = 3


    for rodada in range(1,total_de_tentativas +1):
        print('Tentativas {} de {}'.format(rodada,total_de_tentativas))
        chute = input('Digite o seu numero entre 1 e 50: ')
        
        print("Você digitou ", chute)
        chute = int(chute)
    

        if(chute<1 or chute >50):
            print("Você deve digitar um número entre 1 e 50")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto

        if(acertou): 
            print('Você acertou o numero! E fez {} pontos.'.format(pontuacao))
            break
        
        
        else:
            if(maior): 
                print('Você errou! O seu chute foi maior que o número secreto!')
            else:
                print('Você errou! O seu chute foi menor que o número secreto!')
            pontos_perdidos = abs(numero_secreto - chute)
            pontuacao = pontuacao - pontos_perdidos

    print('Fim do jogo!')