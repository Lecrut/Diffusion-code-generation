def generate_reverse_triangle(height):
    lines = []
    for i in range(height, 0, -1):
        line = ""
        for j in range(i):
            line += str(i)
        lines.append(line)
    return lines

if __name__ == '__main__':
    triangle_height = 5
    result = generate_reverse_triangle(triangle_height)
    for line in result:
        print(line)