def generate_star_pattern(height):
    pattern = []
    for i in range(height):
        spaces = " " * (height - 1 - i)
        stars = "*" * (2 * i + 1)
        pattern.append(spaces + stars)
    return pattern

if __name__ == '__main__':
    height = 4
    pyramid_pattern = generate_star_pattern(height)
    for line in pyramid_pattern:
        print(line)