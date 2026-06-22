def generate_reverse_triangle(height):
    rows = []
    for i in range(height):
        row_values = []
        for j in range(height - i):
            row_values.append(str(height - i))
        rows.append(" ".join(row_values))
    return "\n".join(rows)

if __name__ == '__main__':
    triangle_height = 5
    result = generate_reverse_triangle(triangle_height)
    print(result)