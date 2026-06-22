def rectangle_generator(rows, cols, symbol):
    for r in range(rows):
        yield symbol * cols

if __name__ == '__main__':
    R = 6
    C = 8
    S = '+'
    result = ''.join(rectangle_generator(R, C, S))
    print(result)