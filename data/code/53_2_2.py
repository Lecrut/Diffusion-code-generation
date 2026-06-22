def reverse_number_triangle(height=6):
    rows = []
    for i in range(height, 0, -1):
        row_strs = []
        for j in range(1, i + 1):
            row_strs.append(str(j))
        rows.append(" ".join(row_strs))
    return rows

if __name__ == '__main__':
    result = reverse_number_triangle(6)
    print(result)