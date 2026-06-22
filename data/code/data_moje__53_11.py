def generate_reverse_number_triangle(height):
    lines = []
    for row in range(1, height + 1):
        line = "".join(str(j) for j in range(1, row + 1))
        lines.append(line)
    lines.reverse()
    return "\n".join(lines)

if __name__ == '__main__':
    height = 5
    result = generate_reverse_number_triangle(height)
    print(result)