def checkerboard_generator(n):
    for i in range(n):
        row = ['B' if (i + j) % 2 == 0 else 'W' for j in range(n)]
        yield row

if __name__ == '__main__':
    gen = checkerboard_generator(8)
    for _ in range(4):
        print(next(gen))