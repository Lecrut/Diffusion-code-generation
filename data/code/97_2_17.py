def generate_truth_table(inputs):
    n = len(inputs)
    num_rows = 2 ** n
    header = " | ".join(inputs)
    print(header)
    print("-" * len(header))
    for i in range(num_rows):
        row_values = []
        for j in range(n):
            bit = (i >> (n - 1 - j)) & 1
            row_values.append(str(bool(bit)))
        print(" | ".join(row_values))

if __name__ == '__main__':
    inputs = ["A", "B", "C"]
    generate_truth_table(inputs)