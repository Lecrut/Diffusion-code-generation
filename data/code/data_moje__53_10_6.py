def generate_reverse_number_triangle(n):
    result = []
    for i in range(n, 0, -1):
        row = []
        for j in range(i, 0, -1):
            row.append(str(j))
        result.append(" ".join(row))
    return "\n".join(result)

if __name__ == '__main__':
    value = 5
    output = generate_reverse_number_triangle(value)
    print(output)