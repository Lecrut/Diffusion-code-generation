def rectangle_generator(rows, cols, symbol):
    return [symbol * cols for _ in range(rows)]

if __name__ == '__main__':
    R = 5
    C = 10
    S = '*'
    result = rectangle_generator(R, C, S)
    print(result)