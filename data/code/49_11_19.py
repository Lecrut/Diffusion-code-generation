def generate_square_pattern(size=10):
    return '\n'.join([''.join(['*' for _ in range(size)]) for _ in range(size)])

if __name__ == '__main__':
    print(generate_square_pattern(10))