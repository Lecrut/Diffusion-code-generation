def checkerboard_generator():
    row = 0
    while True:
        yield [row % 2 for _ in range(8)]
        row += 1
if __name__ == '__main__':
    board_gen = checkerboard_generator()
    print(next(board_gen))
    print(next(board_gen))