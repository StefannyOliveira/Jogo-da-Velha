from random import choice


def display_board(board):
    for linha in board:
        print(linha)
    print()

def enter_move(board):
    jogador_move = input("Digite o número da célula para fazer a sua jogada (1 a 9): ")

    if jogador_move.isdigit():
        jogador_move = int(jogador_move)
        i = (jogador_move - 1) // 3
        j = (jogador_move - 1) % 3

        if board[i][j] not in ['O', 'X']:
            board[i][j] = 'O'
        else:
            print("Célula ocupada. Por favor, escolha uma célula válida.")
            enter_move(board)
    else:
        print("Entrada inválida. Por favor, digite um número de 1 a 9.")
        enter_move(board)

def make_list_of_free_fields(board):
	disponiveis = []	
	for i in range(3):
		for j in range(3):
			if board[i][j] not in ['O','X']:
				disponiveis.append((i,j))
	return disponiveis

def victory_for(board, sign):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign or \
           board[0][i] == board[1][i] == board[2][i] == sign:
            return 'Você venceu!' if sign == 'O' else 'Você perdeu!'

        if board[0][0] == board[1][1] == board[2][2] == sign or \
           board[0][2] == board[1][1] == board[2][0] == sign:
            return 'Você venceu!' if sign == 'O' else 'Você perdeu!'

    return None

def draw_move(board):
    disponiveis = make_list_of_free_fields(board)
    if disponiveis:
        i, j = choice(disponiveis)
        board[i][j] = 'X'


board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] 
board[1][1] = 'X'
jogador = True
disponiveis = make_list_of_free_fields(board)

while len(disponiveis):
    display_board(board)
     
    if jogador:
        enter_move(board)
    else:
        print("Agora é a vez da máquina...")
        draw_move(board)

    resultado = victory_for(board, 'O')
    if resultado:
        print(resultado)
        break

    resultado = victory_for(board, 'X')
    if resultado:
        print(resultado)
        break

    disponiveis = make_list_of_free_fields(board)
    jogador = not jogador

if not disponiveis:
    print("Empate! O jogo terminou sem vencedor.")