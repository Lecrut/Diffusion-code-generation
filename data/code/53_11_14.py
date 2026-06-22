def generate_reverse_number_triangle(height):
    lines = []
    for row in range(1, height + 1):
        line = ''.join(str(i) for i in range(row, 0, -1))
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    triangle_height = 5
    result = generate_reverse_number_triangle(triangle_height)
    print(result)