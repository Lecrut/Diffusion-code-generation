def print_stars_pattern(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    [print('*' * (i + 1)) for i in range(n)]

if __name__ == '__main__':
    print_stars_pattern(5)