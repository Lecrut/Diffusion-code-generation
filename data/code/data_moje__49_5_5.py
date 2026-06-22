def print_square_pattern(n):
    pattern = ['*' * n for _ in range(n)]
    for row in pattern:
        print(row)

if __name__ == '__main__':
    print_square_pattern(8)