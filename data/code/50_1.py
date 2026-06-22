def generate_isosceles_triangle(height):
    lines = []
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    height = 7
    result = generate_isosceles_triangle(height)
    print(result)