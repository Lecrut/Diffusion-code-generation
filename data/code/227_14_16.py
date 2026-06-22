def print_stars_pattern(n):
    if not isinstance(n, int) or n <= 0:
        return
    
    pattern = [('*' * i).ljust(n) for i in range(1, n + 1)]
    for line in pattern:
        print(line)

if __name__ == '__main__':
    print_stars_pattern(5)