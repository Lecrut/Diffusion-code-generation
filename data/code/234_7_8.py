def checkerboard_generator(n):
    for i in range(n):
        row = ['W' if (i + j) % 2 == 0 else 'B' for j in range(n)]
        yield row

if __name__ == '__main__':
    gen = checkerboard_generator(5)
    for _ in range(5):
        print(next(gen))