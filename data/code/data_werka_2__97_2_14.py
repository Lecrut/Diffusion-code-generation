def generate_truth_table(inputs):
    n = len(inputs)
    num_rows = 1 << n
    header = " | ".join(inputs)
    print(header)
    print("-" * len(header))
    for i in range(num_rows):
        row_vals = []
        for j in range(n):
            bit = (i >> (n - 1 - j)) & 1
            row_vals.append(str(bool(bit)))
        print(" | ".join(row_vals))

if __name__ == '__main__':
    inputs = ["P", "Q"]
    generate_truth_table(inputs)