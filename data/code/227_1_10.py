def generate_star_pattern(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Height must be a positive integer")
    
    pattern = []
    for i in range(n):
        spaces = " " * (n - 1 - i)
        stars = "*" * (2 * i + 1)
        pattern.append(spaces + stars)
    
    return pattern

if __name__ == '__main__':
    height = 4
    try:
        star_pattern = generate_star_pattern(height)
        for line in star_pattern:
            print(line)
    except ValueError as e:
        print(e)