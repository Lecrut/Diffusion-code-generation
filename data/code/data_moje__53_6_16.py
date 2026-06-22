def generate_reverse_triangle(height):
    lines = []
    for i in range(height, 0, -1):
        line = ""
        for j in range(1, i + 1):
            line += str(j)
            if j != i:
                line += " "
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    print(generate_reverse_triangle(4))