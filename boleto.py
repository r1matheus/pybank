def linha():
    print('*' * 25)


# Alterar se necessario
usuario = 'Glauco'
saldo = 1500.00



# Menu Principal
print('PyBank - Menu Principal')
linha()
print(f'Olá {usuario}')
linha()
print(f'''Saldo : R${saldo}
[1] Pagar
[2] Sair''')

# Valores e Jros
valor_net = 178.80
valor_claro = 259.00
valor_unisan = 218.00
juros_pix = 0.10

while True:
    opcao = int(input('Selecione uma opção: '))
    linha()

    if opcao == 1:
        print('''Contas pendentes:
[1] Net Servicos
[2] Claro S/A
[3] Unisan''' )
    
    # Selecao dos boletos
        opc_pagamento = int(input('Selecione a conta que deseja pagar: '))
        linha()
        if opc_pagamento == 1:
            print('Boleto Net')
            break
        if opc_pagamento == 2:
            print('Boleto claro')
            break
        if opc_pagamento == 3:
            print('Boleto Unisan')
            break
            
    elif opcao == 2:
        exit()
            
    else:
        print('Dados invalidos')

forma_pagamento = int(input('''Formas de pagamento:
[1] PIX
[2] Débito na conta
[3] Carnê
Escolha uma opcao: '''))
    
linha()
if forma_pagamento == 1 and opc_pagamento == 1:
    print('Pago!')
    pag_final = saldo - valor_net * juros_pix
    print(f'Saldo atual: {pag_final}')

linha()
print('PROGRAMA ENCERRADO')