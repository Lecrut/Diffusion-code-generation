def generate_reverse_number_triangle(rows=5):
    result = []
    for i in range(rows, 0, -1):
        row = []
        for j in range(1, i + 1):
            row.append(j)
        result.append(row)
    return result

if __name__ == '__main__':
    print(generate_reverse_number_triangle(5))