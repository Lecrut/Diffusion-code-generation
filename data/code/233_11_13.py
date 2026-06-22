SYMBOL_TABLE = {
    'star': '*',
    'hash': '#',
    'plus': '+'
}

def generate_symbol_matrix(rows, cols, symbol_type):
    symbol = SYMBOL_TABLE.get(symbol_type, '*')
    return '\n'.join([symbol * cols for _ in range(rows)])

if __name__ == '__main__':
    matrix = generate_symbol_matrix(5, 10, 'hash')
    print(matrix)