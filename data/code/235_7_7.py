def checkerboard(size):
    pattern = []
    for i in range(size):
        row = []
        for j in range(size):
            if (i + j) % 2 == 0:
                row.append('X')
            else:
                row.append('.')
        pattern.append(row)
    return pattern

if __name__ == '__main__':
    size = 4
    board = checkerboard(size)
    for row in board:
        print(''.join(row))