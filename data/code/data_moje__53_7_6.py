def generate_reverse_number_triangle(rows):
    triangle_lines = []
    for i in range(rows, 0, -1):
        line = ' '.join(str(j) for j in range(1, i + 1))
        triangle_lines.append(line)
    return '\n'.join(triangle_lines)

if __name__ == '__main__':
    result = generate_reverse_number_triangle(6)
    print(result)