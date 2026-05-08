def generate_truth_table(input_vars):
    num_vars = len(input_vars)
    num_rows = 2**num_vars
    if num_vars == 0:
        num_rows = 1
    header = " | ".join(str(f"V{i+1}") for i in range(num_vars))
    print(header)
    print("-" * len(header))
    for i in range(num_rows):
        row_values = []
        for j in range(num_vars):
            if (i >> j) & 1:
                row_values.append("T")
            else:
                row_values.append("F")
        print(" | ".join(row_values))
if __name__ == '__main__':
    sample_inputs = [0, 0, 0]
    generate_truth_table(sample_inputs)