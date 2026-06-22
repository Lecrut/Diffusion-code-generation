def generate_isosceles_triangle():
    height = 7
    lines = []
    for i in range(height):
        num_spaces = height - 1 - i
        num_stars = 2 * i + 1
        line = ' ' * num_spaces + '*' * num_stars
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_isosceles_triangle())