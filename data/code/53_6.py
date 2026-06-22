def generate_reverse_triangle(height):
    lines = []
    for i in range(height, 0, -1):
        row = ' '.join(str(i) for _ in range(i))
        lines.append(row)
    return '\n'.join(lines)

if __name__ == '__main__':
    height = 4
    result = generate_reverse_triangle(height)
    print(result)