def generate_square_pattern(size):
    return '\n'.join('*' * size for _ in range(size))

if __name__ == '__main__':
    result = generate_square_pattern(10)
    print(result)