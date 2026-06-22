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
    return '\n'.join([''.join(row) for row in board])

if __name__ == '__main__':
    checkerboard = generate_checkerboard(4)
    print(checkerboard)