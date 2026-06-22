def reverse_number_triangle(height=6):
    lines = []
    for row in range(height, 0, -1):
        line = ""
        for num in range(1, row + 1):
            line += str(num)
        lines.append(line)
    return lines

if __name__ == '__main__':
    result = reverse_number_triangle()
    for line in result:
        print(line)