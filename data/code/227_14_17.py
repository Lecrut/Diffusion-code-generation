def print_stars_pattern(n):
    for i in range(1, n + 1):
        line = ''.join('*' if j < i else ' ' for j in range(n))
        print(line)

if __name__ == '__main__':
    pattern_size = 7
    print_stars_pattern(pattern_size)