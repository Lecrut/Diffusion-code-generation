def generate_square_pattern():
    return '\n'.join(['*' * 10 for _ in range(10)])

if __name__ == '__main__':
    print(generate_square_pattern())