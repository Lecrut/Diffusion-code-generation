def checkerboard_generator(size):
    for row in range(size):
        yield [1 if (row + col) % 2 == 0 else 0 for col in range(size)]

if __name__ == '__main__':
    board = checkerboard_generator(8)
    print(next(board))
    print(next(board))