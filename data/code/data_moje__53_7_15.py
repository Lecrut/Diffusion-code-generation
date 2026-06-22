def generate_reverse_number_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        row_values = []
        for j in range(i, 0, -1):
            row_values.append(str(j))
        result.append(" ".join(row_values))
    return "\n".join(result)

if __name__ == '__main__':
    print(generate_reverse_number_triangle(6))