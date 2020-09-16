#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************\n\n")

print('Selecione o número da operação desejada:\n')

print('1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão')


# In[ ]:


escolha = input('Digite sua opção(1/2/3/4):')

num1 = float(input('Digite o primeiro número:'))

num2 = float(input('Digite o segundo número:'))


# In[ ]:


if escolha =='1':
    resultsoma = num1 + num2
    print('A soma dos números %s e %r dá: '%(num1, num2), resultsoma)
elif escolha =='2':
    resultsub = num1 - num2
    print('A subtração dos números %s e %r dá:'%(num1, num2), resultsub)
elif escolha =='3':
    resultmult = num1*num2
    print('A multiplicação dos números %s e %r dá:'%(num1, num2), resultmult)
else: 
    resultdiv = num1/num2
    print('A divisão dos números %s e %r dá:'%(num1, num2),resultdiv)
    
    


# In[ ]:




