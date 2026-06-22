def generate_symbol_matrix(rows, cols, symbol):
    return '\n'.join([' '.join([symbol] * cols) for _ in range(rows)])

if __name__ == '__main__':
    matrix = generate_symbol_matrix(5, 10, '*')
    print(matrix)