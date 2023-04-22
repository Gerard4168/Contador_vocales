# Se ingresa una frase y el programa nos dice cuantas vocales hay en una frase.

print('======================================================')
texto=input('Escriba una frase: ')
print('======================================================')

vocal1 = "a"
vocal2 = "e"
vocal3 = 'i'
vocal4 = 'o'
vocal5 = 'u'

a = 0
e = 0
y = 0
o = 0
u = 0

for i in texto:
    if i in vocal1:
     a += 1
    elif i in vocal2:
       e += 1
    elif i in vocal3:
       y += 1
    elif i in vocal4:
       o += 1
    elif i in vocal5:
       u += 1
print('======================================================')
print('La cantidad de a que hubo en la frase fue de: '+ str(a))
print('La cantidad de e que hubo en la frase fue de: '+ str(e))
print('La cantidad de i que hubo en la frase fue de: '+ str(y))
print('La cantidad de o que hubo en la frase fue de: '+ str(o))
print('La cantidad de u que hubo en la frase fue de: '+ str(u))
print('======================================================')