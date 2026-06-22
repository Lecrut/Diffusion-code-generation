def generate_square_pattern(size=6):
    row = '*' * size
    pattern = '\n'.join([row] * size)
    return pattern
if __name__ == '__main__':
    result = generate_square_pattern(6)
    print(result)