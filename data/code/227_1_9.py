def generate_star_pattern(n):
    pattern = []
    for i in range(n):
        spaces = " " * (n - 1 - i)
        stars = "*" * (2 * n - 1 - 2 * i)
        pattern.append(spaces + stars)
    return pattern

if __name__ == '__main__':
    height = 4
    star_pattern = generate_star_pattern(height)
    for line in star_pattern:
        print(line)