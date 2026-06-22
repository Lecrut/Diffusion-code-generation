def generate_reverse_number_triangle(rows):
    result = []
    for i in range(1, rows + 1):
        row = []
        for j in range(i, 0, -1):
            row.append(str(j))
        result.append(' '.join(row))
    return result

if __name__ == '__main__':
    rows = 5
    lines = generate_reverse_number_triangle(rows)
    for line in lines:
        print(line)