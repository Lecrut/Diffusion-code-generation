def generate_reverse_number_triangle(height=4):
    lines = []
    for row in range(height, 0, -1):
        line = ' '.join(str(i) for i in range(1, row + 1))
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_reverse_number_triangle(4)
    print(result)