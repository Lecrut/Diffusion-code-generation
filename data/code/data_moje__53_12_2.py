def construct_reverse_number_triangle(n):
    rows = []
    for i in range(1, n + 1):
        row_numbers = range(i, n + 1)
        row_str = " ".join(str(num) for num in row_numbers)
        rows.append(row_str)
    result = "\n".join(rows)
    return result

if __name__ == '__main__':
    sample_n = 5
    output = construct_reverse_number_triangle(sample_n)
    print(output)