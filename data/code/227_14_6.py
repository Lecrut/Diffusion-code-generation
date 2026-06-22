def print_stars_pattern(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    
    pattern = ['*' * (i + 1) for i in range(n)]
    [print(line) for line in pattern]

if __name__ == '__main__':
    print_stars_pattern(5)