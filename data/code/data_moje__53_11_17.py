def generate_reverse_number_triangle(height):
    lines = []
    for i in range(height, 0, -1):
        line = ""
        for j in range(1, i + 1):
            line += str(j) + " "
        lines.append(line.rstrip())
    return "\n".join(lines)

if __name__ == '__main__':
    triangle_height = 5
    print(generate_reverse_number_triangle(triangle_height))