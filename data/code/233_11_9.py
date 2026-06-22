SYMBOL_PATTERN = {
    'A': '*',
    'B': '#',
    'C': '@'
}

def create_symbol_matrix(rows, cols, pattern_key):
    symbol = SYMBOL_PATTERN.get(pattern_key, '?')
    return '\n'.join([symbol * cols for _ in range(rows)])

if __name__ == '__main__':
    rows_val = 5
    cols_val = 10
    pattern_key_val = 'A'
    result = create_symbol_matrix(rows_val, cols_val, pattern_key_val)
    print(result)