print('ola sejá bem-vindo a loja do adriano oliveira')
#  montando a estrutura
valor_unitario = float(input('entre com o valor do produto R$'))
produtos_adquiridos = int(input('entre com a quantidade do produto'))
# parte referente ao desconto do app
desconto = 0
if produtos_adquiridos >= 1000:
    desconto = 0.00
elif (produtos_adquiridos >= 1000) and (produtos_adquiridos < 3000):
    desconto = 0.03
elif (produtos_adquiridos >= 3000) and (produtos_adquiridos < 5000):
    desconto = 0.05
else:
    desconto = 0.08

valor_sem_desconto = valor_unitario * produtos_adquiridos
print('valor sem desconto é de r$ {:.2f}'.format(valor_sem_desconto))
valor_com_desconto = valor_sem_desconto - valor_sem_desconto * desconto
print('valor com desconto é de r$ {:.2f}'.format(valor_com_desconto))
