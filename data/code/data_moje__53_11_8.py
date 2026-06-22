def generate_reverse_number_triangle(height):
    lines = []
    for i in range(height, 0, -1):
        line = ' '.join(str(i) for _ in range(i))
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    triangle_height = 5
    result = generate_reverse_number_triangle(triangle_height)
    print(result)