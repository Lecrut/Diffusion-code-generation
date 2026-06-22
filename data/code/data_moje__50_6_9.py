def generate_star_triangle(height):
    result = []
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        stars = '*' * (2 * i + 1)
        result.append(spaces + stars)
    return '\n'.join(result)

if __name__ == '__main__':
    height = 6
    output = generate_star_triangle(height)
    print(output)