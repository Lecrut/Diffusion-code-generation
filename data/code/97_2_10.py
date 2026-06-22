def generate_truth_table(inputs):
    n = len(inputs)
    total_rows = 1 << n
    header = " | ".join(inputs)
    print(header)
    print("-" * len(header))
    for i in range(total_rows):
        row_values = []
        for j in range(n):
            bit = (i >> (n - 1 - j)) & 1
            row_values.append(str(bool(bit)))
        row_str = " | ".join(row_values)
        print(row_str)

if __name__ == '__main__':
    generate_truth_table(["A", "B", "C"])