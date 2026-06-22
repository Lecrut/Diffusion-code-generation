def generate_reverse_number_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        row = []
        for j in range(i, 0, -1):
            row.append(j)
        result.append(row)
    return result

if __name__ == '__main__':
    rows = 5
    print(generate_reverse_number_triangle(rows))