def generate_truth_table(input_vars):
    num_vars = len(input_vars)
    num_rows = 2 ** num_vars
    if num_vars == 0:
        num_rows = 1
    header = [f"Input {i+1}" for i in range(num_vars)]
    header.append("Output")
    print(" | ".join(header))
    print("-" * (len(" | ".join(header)) + 3))
    for i in range(num_rows):
        row_values = []
        for j in range(num_vars):
            if (i >> j) & 1:
                row_values.append('T')
            else:
                row_values.append('F')
        output_value = 'F'
        if all(row_values):
            output_value = 'T'
        print(" | ".join(row_values + [output_value]))
if __name__ == '__main__':
    sample_inputs = [0, 0, 0]
    generate_truth_table(sample_inputs)