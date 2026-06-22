def checkerboard_generator(n):
    for i in range(n):
        row = ['X' if (i + j) % 2 == 0 else 'O' for j in range(n)]
        yield row

if __name__ == '__main__':
    board = checkerboard_generator(5)
    for row in board:
        print(row)