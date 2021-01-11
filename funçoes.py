def calcular_media(notas):
    quantidade = len(notas)
    soma = sum(notas)
    media = soma / quantidade
    print('o aluno tirou',media)
    return media

def verificar_aprovacao(media):
   if media >=6:
       print('aluno aprovado')
   else:
       print('aluno reprovado')  

 notas = [ 12 , 5 , 1 ]
 quantidade = len(notas)
 soma = sum(notas)
 media = soma / quantidade
 print( 'o aluno tirou', media)
 verificar_aprovacao(media)
