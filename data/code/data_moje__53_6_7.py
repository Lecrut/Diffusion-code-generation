def generate_reverse_triangle(height):
    lines = []
    for i in range(height, 0, -1):
        line = " ".join(str(j) for j in range(i, 0, -1))
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    result = generate_reverse_triangle(4)
    print(result)