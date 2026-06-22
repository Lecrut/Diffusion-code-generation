def generate_symbol_matrix(rows, cols, symbol):
    if rows < 1 or cols < 1:
        raise ValueError("Rows and columns must be positive integers.")
    return '\n'.join([symbol * cols for _ in range(rows)])

if __name__ == '__main__':
    matrix = generate_symbol_matrix(5, 10, '*')
    print(matrix)