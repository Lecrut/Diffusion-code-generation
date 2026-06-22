def generate_square_pattern(size):
    return '\n'.join(['*' * size] * size)
if __name__ == '__main__':
    print(generate_square_pattern(6))