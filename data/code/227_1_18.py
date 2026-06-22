def generate_star_pattern(height):
    pattern = []
    for i in range(height):
        spaces = " " * (height - 1 - i)
        stars = "*" * (2 * i + 1)
        pattern.append(spaces + stars)
    return pattern

if __name__ == '__main__':
    sample_height = 4
    star_pattern = generate_star_pattern(sample_height)
    for line in star_pattern:
        print(line)