def rectangle_generator(rows, cols, symbol):
    for r in range(rows):
        for c in range(cols):
            yield symbol
if __name__ == '__main__':
    R = 5
    C = 10
    S = '*'
    gen = rectangle_generator(R, C, S)
    result = list(gen)
    print(result)