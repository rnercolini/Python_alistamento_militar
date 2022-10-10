# Analisa a idade conforme o ano do nascimento e retorna com informações sobre o alistamento militar.
from datetime import date
print('\033[32m<=====ALISTAMENTO MILITAR=====>\033[m')
print('\033[32m-+-\033[m' * 20)
ano = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - ano
print('\033[32m-+-\033[m' * 20)
print('Você nasceu no ano de {}, tem {} anos em {}.'.format(ano, idade, date.today().year))
if idade < 18:
    print('Falta(m) \033[4;31m{}\033[m ano(s) para o seu alistamento.'.format(18 -idade))
elif idade == 18:
    print('\033[4;31mATENÇÃO:\033[m Você precisa se alistar este ano.')
else:
    print('\033[4;31mATENÇÃO:\033[m Você já deveria ter se alistado há \033[4;31m{}\033[m ano(s).'.format(idade - 18))
