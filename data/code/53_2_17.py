def reverse_number_triangle(height):
    lines = []
    for i in range(height, 0, -1):
        line = ""
        count = 0
        for j in range(i):
            line += str(count)
            count += 1
        lines.append(line)
    return lines

if __name__ == '__main__':
    height = 6
    result = reverse_number_triangle(height)
    print(result)