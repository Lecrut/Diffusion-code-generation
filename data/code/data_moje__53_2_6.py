def generate_reverse_triangle(height):
    lines = []
    for i in range(height, 0, -1):
        line = ""
        for j in range(i, 0, -1):
            line += str(j)
        lines.append(line)
    return lines

if __name__ == '__main__':
    result = generate_reverse_triangle(6)
    for line in result:
        print(line)