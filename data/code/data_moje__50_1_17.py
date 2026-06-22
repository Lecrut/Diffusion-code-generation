def generate_isosceles_triangle(height):
    if height < 1:
        return ""
    lines = []
    total_width = 2 * height - 1
    for row in range(1, height + 1):
        star_count = 2 * row - 1
        padding = (total_width - star_count) // 2
        line = ' ' * padding + '*' * star_count
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    HEIGHT = 7
    triangle = generate_isosceles_triangle(HEIGHT)
    print(triangle)