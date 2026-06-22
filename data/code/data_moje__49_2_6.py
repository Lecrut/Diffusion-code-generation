def print_square(size):
    return '\n'.join(['*' * size for _ in range(size)])

if __name__ == '__main__':
    size = 7
    result = print_square(size)
    print(result)