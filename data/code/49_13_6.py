def generate_square_pattern(size=6):
    row = '*' * size
    return '\n'.join([row] * size)
if __name__ == '__main__':
    pattern = generate_square_pattern()
    print(pattern)