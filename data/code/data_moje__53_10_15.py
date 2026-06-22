def generate_reverse_number_triangle(n: int) -> list[str]:
    rows = []
    for i in range(n, 0, -1):
        row_nums = []
        for j in range(1, i + 1):
            row_nums.append(str(j))
        rows.append(" ".join(row_nums))
    return rows

if __name__ == '__main__':
    result = generate_reverse_number_triangle(5)
    print(result)