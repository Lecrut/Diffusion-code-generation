def checkerboard_generator(n):
    pattern = {0: ' ', 1: '#'}
    for i in range(n * n):
        yield pattern[i % 2]

if __name__ == '__main__':
    board_gen = checkerboard_generator(4)
    for _ in range(16):
        print(next(board_gen), end='')
        if (_ + 1) % 4 == 0:
            print()