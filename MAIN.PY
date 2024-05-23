# entrada de dados
nome = input('informe o seu nome: ')
idade = int(input ('informe a sua idade:'))

if idade <=12:
    print(f'Desculpe sua idade não esta dentro da classificação obrigatória.')
else:

#lista de filmes, classificação e suas salas
    print('LISTA DE FILMES\n')
    print('Sala 1 - O Poderoso Chefão, idade miníma = 14' )
    print('Sala 2 - O Quarto de Jack, idade miníma = 14')
    print('Sala 3 - Capitão América, idade miníma = 12.')
    print('Sala 4 - Nasce Uma Estrela, idade miníma = 16')
    print('Sala 5 - As Branquelas, idade miníma = 18.')

while True:
        #recebe a sala escolhida
        sala = int(input('informe a sala desejada: '))

        match sala:
            case 1: 
                if idade >= 14:
                    print(f'filme escolhido por {nome}: O Poderoso Chefão. Entrada liberada') 
                    break
                elif idade <=14:
                    print(f'{nome} Entrada negada, escolha novamente')
                    continue
            case 2: 
                if idade >=14:
                    print(f'Filme escolhido por {nome}: O Quarto de Jack. Entrada liberada') 
                    break
                elif idade <=14:
                    print(f'{nome} Entrada negada, escolha novamente')
                    continue
            case 3:
                if idade >= 12:
                    print(f'Filme escolhido por {nome}: Capitão América. Entrada liberada')
                    break
                elif idade <=12:
                    print(f'{nome} Entrada negada, escolha novamente')
                    continue
            case 4:
                if idade >= 16:
                    print(f'Filme escolhido por {nome}: Nasce Uma Estrela. Entrada liberada')
                    break
                elif idade <=16:
                    print(f'{nome} Entrada negada, escolha novamente')
                    continue
            case 5:
                if idade >=18:
                    print(f'Filme escolhido por {nome}: As Branquelas. Entrada liberada')
                    break
                elif idade <=16:
                    print(f'{nome} Entrada negada, escolha novamente')
                    continue
            case _:
                    print('Sala inexistente.')
            
    # pergunta para o usuário se deseja continuar ou encerrar
        continuar = input('deseja continuar (s/n)? ')

    #verifica a opção do usuário

        if continuar == 's':
            continue
        elif continuar == 'n':
            break
        else:
            print('opção inválida')
        continue

                    