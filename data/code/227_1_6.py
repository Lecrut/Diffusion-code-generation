def generate_star_pattern(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    pattern = []
    for i in range(n):
        spaces = " " * (n - 1 - i)
        stars = "*" * (2 * i + 1)
        pattern.append(spaces + stars)
    
    return pattern

if __name__ == '__main__':
    height = 4
    pyramid_pattern = generate_star_pattern(height)
    for line in pyramid_pattern:
        print(line)