def print_stars_pattern(n):
    [print('*' * (i + 1)) for i in range(n)]

if __name__ == '__main__':
    n_size = 7
    print_stars_pattern(n_size)