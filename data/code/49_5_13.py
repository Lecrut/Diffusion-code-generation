def print_square_stars(n=8):
    rows = [[print('*', end='') for _ in range(n)] for _ in range(n)]
    print()
    return rows

if __name__ == '__main__':
    result = print_square_stars(8)