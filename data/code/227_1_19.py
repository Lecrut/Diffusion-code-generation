def generate_star_pyramid(height):
    pyramid = []
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        pyramid.append(spaces + stars)
    return pyramid

if __name__ == '__main__':
    print(generate_star_pyramid(4))