def print_stars_pattern(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    pattern = [('*' * (i + 1)) for i in range(n)]
    for line in pattern:
        print(line)

if __name__ == '__main__':
    try:
        print_stars_pattern(5)
    except ValueError as e:
        print(e)