

opradora = []
def opradora_vivo():
    numero_tele = input('Numero do telefone: ')
    while True:
        valor_tel = input('Valor: ')
        try:
            valor = float(valor_tel)
            if valor >= 10:
                print('Recarga com sucesso!')
                break

            else:
                print('Valor minimo para recarga é R$10,00.')
        except ValueError:
            print('Erro: informe um valor numerico valido!')



def operadora_claro():
    numero_tele = input('Numero do telefone: ')
    valor_tel = input('Valor: ')
    while True:
        try:
            valor = float(valor_tel)
            if valor >= 10:
                print('Recarga com sucesso!')
                break

            else:
                print('Valor minimo para recarga é R$10,00.')
        except ValueError:
            print('Erro: informe um valor numerico valido!')


def operadora_tim():
    numero_tele = input('Numero do telefone: ')
    while True:
        valor_tel = input('Valor: ')
        try:
            valor = float(valor_tel)
            if valor >= 10:
                print('Recarga com sucesso!')
                break

            else:
                print('Valor minimo para recarga é R$10,00.')
        except ValueError:
            print('Erro: informe um valor numerico valido!')


def menu():
    while True:
        print('''Opção
        1 - Vivo
        2 - Claro
        3 - Tim''')

        opção = input('Qual operadora: ')
        if opção == '1':
            opradora_vivo()

            break

        elif opção == '2':
            operadora_claro()
            break

        elif opção == '3':
            operadora_tim()
            break
menu()
