def reverse_number_triangle(height=4):
    lines = []
    for i in range(height, 0, -1):
        row = ''
        for j in range(1, i + 1):
            row += str(j)
        lines.append(row)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(reverse_number_triangle())