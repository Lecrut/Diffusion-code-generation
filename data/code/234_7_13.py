def checkerboard_generator(size):
    for i in range(size):
        yield [i % 2 == j % 2 for j in range(size)]

if __name__ == '__main__':
    board = checkerboard_generator(10)
    for row in next(board):
        print(row)