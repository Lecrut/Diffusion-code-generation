def generate_pyramid_star_pattern(height):
    pattern = []
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        pattern.append(spaces + stars)
    return pattern

if __name__ == '__main__':
    pyramid = generate_pyramid_star_pattern(4)
    for line in pyramid:
        print(line)