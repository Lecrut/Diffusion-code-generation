def generate_reverse_number_triangle(height=4):
    lines = []
    for row in range(height, 0, -1):
        line = ""
        for col in range(1, row + 1):
            line += str(col) + " "
        lines.append(line.strip())
    return "\n".join(lines)

if __name__ == '__main__':
    result = generate_reverse_number_triangle(4)
    print(result)