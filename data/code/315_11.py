def generate_pattern(n, symbol):
    row = symbol * n
    pattern = row * n
    return pattern
if __name__ == '__main__':
    N = 3
    S = '*'
    result = generate_pattern(N, S)
    print(result)