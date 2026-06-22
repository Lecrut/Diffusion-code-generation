def generate_symmetric_reverse_number_triangle(rows):
    lines = []
    for i in range(1, rows + 1):
        left_part = []
        for num in range(i, 0, -1):
            left_part.append(str(num))
        right_part = []
        for num in range(2, i + 1):
            right_part.append(str(num))
        line = " ".join(left_part + right_part)
        lines.append(line)
    return lines

if __name__ == '__main__':
    triangle_lines = generate_symmetric_reverse_number_triangle(5)
    for line in triangle_lines:
        print(line)