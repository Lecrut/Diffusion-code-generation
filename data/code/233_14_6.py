def build_rectangle(rows, cols, symbol):
    return '\n'.join([symbol * cols for _ in range(rows)])

if __name__ == '__main__':
    R = 3
    C = 7
    S = '+'
    rectangle = build_rectangle(R, C, S)
    print(rectangle)