def generate_isosceles_triangle(height):
    lines = []
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        lines.append(spaces + stars)
    return lines

if __name__ == '__main__':
    height = 7
    triangle = generate_isosceles_triangle(height)
    for line in triangle:
        print(line)