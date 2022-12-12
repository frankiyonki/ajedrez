def partida_ajedrez(nombre_fichero):
# creación tablero con lista separada por lineas con cada elemento
    tablero_inicial = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
# creación tablero para crear filas
    tablero =  []
# bucle que permite partir tablero por \n
    for i in tablero_inicial.split('\n'):
        tablero.append(i.split('\t'))
# creacion archivo para guardar resultados
    f = open(nombre_fichero, 'w')
    for i in tablero:
        f.write('\t'.join(i) + '\n')
    f.close()
    movimiento = 0
# funcion para jugabilidad
    while True:
        continuar = input('Deseas hacer otro movimiento (s/n): ')
        # si responde n partida se acaba y se guarda posiciones
        if continuar == 'n':
            f = open(nombre_fichero, 'r')
            contentf = f.read()
            print(contentf)
            f.close()
            print('partida guardada, hasta luego')
            break
        # si responde s se piden filas y columnas de ficha que se quiere mover y filas y columnas de donde se quiere ir
        elif continuar == 's':
            fila_origen = int(input('Introduce la fila de la pieza a mover: '))
            columna_origen = int(input('Introduce la columna de la pieza a mover: '))
            fila_destino = int(input('Introduce la fila de destino: '))
            columna_destino = int(input('Introduce la columna de destino: '))
            tablero[fila_destino-1][columna_destino-1] = tablero[fila_origen-1][columna_origen-1]
            tablero[fila_origen-1][columna_origen-1] = ''
            movimiento += 1
            f = open(nombre_fichero, 'a')
            f.write('Movimiento' + str(movimiento) + '\n')
            for i in tablero:
                f.write('\t'.join(i) + '\n')
            f.close()
    return

partida_ajedrez('partida-1.txt')
