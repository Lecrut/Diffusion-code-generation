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

if __name__ == '__main__':
    checkerboard = generate_checkerboard(4)
    for row in checkerboard:
        print(''.join(row))