def generate_pyramid_star_pattern(height):
    return [' ' * (height - i - 1) + '*' * (2 * i + 1) for i in range(height)]

if __name__ == '__main__':
    print(generate_pyramid_star_pattern(4))