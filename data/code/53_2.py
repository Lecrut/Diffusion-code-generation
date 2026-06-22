def reverse_number_triangle(height=6):
    lines = []
    for i in range(height, 0, -1):
        line = ''.join(str(j) for j in range(1, i + 1))
        lines.append(line)
    return lines

if __name__ == '__main__':
    result = reverse_number_triangle(6)
    for line in result:
        print(line)