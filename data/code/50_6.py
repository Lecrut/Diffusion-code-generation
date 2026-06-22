def generate_star_triangle(height):
    lines = []
    for i in range(1, height + 1):
        stars = '*' * (2 * i - 1)
        lines.append(stars)
    for i in range(height - 1, 0, -1):
        stars = '*' * (2 * i - 1)
        lines.append(stars)
    return '\n'.join(lines)
if __name__ == '__main__':
    print(generate_star_triangle(6))