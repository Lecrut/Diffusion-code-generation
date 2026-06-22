def generate_reverse_number_triangle(height=6):
    rows = []
    for i in range(height, 0, -1):
        row_str = " ".join(str(j) for j in range(i, 0, -1))
        rows.append(row_str)
    return rows

if __name__ == '__main__':
    print(generate_reverse_number_triangle(6))