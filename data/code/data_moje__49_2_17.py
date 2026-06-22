def print_square(size):
    return '*' * size + '\n' + ('\n'.join('*' * size for _ in range(size - 1)))

if __name__ == '__main__':
    print(print_square(7))