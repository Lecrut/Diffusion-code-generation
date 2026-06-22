def checkerboard_generator(n):
    pattern = {0: ' ', 1: '#'}
    for i in range(n * n):
        yield pattern[i % 2]

if __name__ == '__main__':
    checkerboard = checkerboard_generator(5)
    print("First 25 elements:")
    for _ in range(25):
        print(next(checkerboard), end='')
        if (i + 1) % 5 == 0:
            print()