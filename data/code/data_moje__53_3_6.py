def generate_reverse_number_triangle(rows=5):
    lines = []
    for i in range(rows, 0, -1):
        row_parts = []
        for j in range(1, i + 1):
            row_parts.append(str(j))
        lines.append(" ".join(row_parts))
    return "\n".join(lines)

if __name__ == '__main__':
    result = generate_reverse_number_triangle(5)
    print(result)