def generate_checkerboard(size):
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            if (i + j) % 2 == 0:
                row.append('X')
            else:
                row.append('.')
        board.append(row)
    return board

def print_board(board):
    for row in board:
        print(''.join(row))

if __name__ == '__main__':
    checkerboard = generate_checkerboard(4)
    print_board(checkerboard)