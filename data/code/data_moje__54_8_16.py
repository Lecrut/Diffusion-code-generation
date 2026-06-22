def print_hollow_square(size):
    return '\n'.join([''.join(['*' if row == 0 or row == size - 1 or col == 0 or col == size - 1 else ' ' for col in range(size)]) for row in range(size)])

if __name__ == '__main__':
    result = print_hollow_square(7)
    print(result)