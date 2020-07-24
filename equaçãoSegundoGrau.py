import math

a = float (input ('Digite o valor de a: '))
b = float (input ('Digite o valor de b: '))
c = float (input ('Digite o valor de c: '))


delta = b**2 -4 * a * c

if delta == 0:
    
     r1 = (-b + math.sqrt (delta)) / (2 * a)
     print ('A única raiz é:',r1)


elif delta <0:
    print ('Esta equação não possui raízes reais')
    
else:
    
    r1 = (-b + math.sqrt (delta)) / (2 * a)     
    r2 = (-b - math.sqrt (delta)) / (2 * a)
    print ('A primeira raiz é:',r1)
    print ('A segunda raiz é:',r2)
