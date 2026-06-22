def print_stars_pattern(n):
    [print(' '.join(['*' for _ in range(i)])) for i in range(1, n + 1)]

if __name__ == '__main__':
    pattern_size = 7
    print_stars_pattern(pattern_size)