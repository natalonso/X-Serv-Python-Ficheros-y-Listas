#!/usr/bin/python3

newfd = open('/etc/passwd')

diccionario={}

for line in newfd:

    newfd.readline()
    parts = line.split(':')
    user=parts[0]
    shell=parts[-1]

    print('Usuario: ' + user)
    print('Shell: ' + shell)

    diccionario[user] = shell



busqueda=['root', 'imaginario']

for usuario in busqueda:
    find=diccionario.get(usuario)
    if find == None:
        print('El usuario ' + usuario + ' no ha sido encontrado.')
    else:
        print('El usuario ' + usuario + ' ha sido encontrado: ' + find)
