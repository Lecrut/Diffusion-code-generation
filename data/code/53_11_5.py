def print_reverse_number_triangle(height):
    lines = []
    for i in range(height, 0, -1):
        line = ' '.join((str(j) for j in range(1, i + 1)))
        lines.append(line)
    return '\n'.join(lines)
if __name__ == '__main__':
    triangle_height = 5
    result = print_reverse_number_triangle(triangle_height)
    print(result)