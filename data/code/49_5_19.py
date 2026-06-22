def print_square_pattern(n):
    for _ in range(n):
        print(''.join(['*' for _ in range(n)]))

if __name__ == '__main__':
    print_square_pattern(8)