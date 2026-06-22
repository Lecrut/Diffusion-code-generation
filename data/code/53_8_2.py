def generate_reverse_number_triangle(rows):
    result = []
    for i in range(1, rows + 1):
        row = []
        for j in range(i, 0, -1):
            row.append(j)
        result.append(row)
    return result

if __name__ == '__main__':
    print(generate_reverse_number_triangle(5))