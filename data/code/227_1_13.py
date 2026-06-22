MAX_HEIGHT = 4

def generate_star_pattern(height):
    pattern = []
    for i in range(height):
        spaces = " " * (height - 1 - i)
        stars = "*" * (2 * i + 1)
        pattern.append(spaces + stars)
    return pattern

if __name__ == '__main__':
    star_pattern = generate_star_pattern(MAX_HEIGHT)
    for line in star_pattern:
        print(line)