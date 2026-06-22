def generate_reverse_triangle(height):
    lines = []
    for row in range(height, 0, -1):
        spaces = " " * (height - row)
        stars = "*" * (2 * row - 1)
        lines.append(spaces + stars)
    return lines

if __name__ == '__main__':
    sample_height = 6
    result = generate_reverse_triangle(sample_height)
    for line in result:
        print(line)