nome = input('Qual seu Nome? ')
idade = int(input('Qual sua Idade? '))
# Bloco condicional
if idade > 15 and idade < 18:
    print('Voçê pode votar {}, Porém seu voto é facultativo!'.format(nome))
elif idade >= 18 and idade <= 70:
    print('Voçê pode votar {}, E seu voto é Obrigatório!'.format(nome))
elif idade > 70:
    print('Voçê pode votar {}, Porém seu voto é facultativo!'.format(nome))
else:
    print('Não Pode Votar!')
    