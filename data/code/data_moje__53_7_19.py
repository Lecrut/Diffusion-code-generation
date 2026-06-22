def generate_reverse_number_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        row_numbers = []
        for j in range(1, i + 1):
            row_numbers.append(str(j))
        result.append(" ".join(row_numbers))
    return result

if __name__ == '__main__':
    rows = 6
    output = generate_reverse_number_triangle(rows)
    for line in output:
        print(line)