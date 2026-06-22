def generate_diamond_pattern(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer.")
    
    pattern = []
    for i in range(2 * n - 1):
        spaces = abs(n - i - 1)
        bars = 2 * (i % (n - 1)) + 1
        line = ' ' * spaces + '|' * bars
        pattern.append(line)
    
    return pattern

if __name__ == '__main__':
    n = 5
    diamond_pattern = generate_diamond_pattern(n)
    for line in diamond_pattern:
        print(line)