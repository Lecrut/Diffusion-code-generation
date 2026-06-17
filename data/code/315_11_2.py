def generate_pattern(n, symbol):
    row = symbol * n
    pattern = row * n
    return pattern
if __name__ == '__main__':
    n_val = 3
    symbol_val = '*'
    result = generate_pattern(n_val, symbol_val)
    print(result)