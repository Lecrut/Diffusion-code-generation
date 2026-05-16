def print_truth_table(input_combinations):
    if not input_combinations:
        return
    num_inputs = len(input_combinations)
    num_combinations = 2 ** num_inputs
    print("Truth Table:")
    headers = [f"Input {i+1}" for i in range(num_inputs)]
    header_line = " | ".join(headers)
    print("-" * (len(header_line) + 3 * num_inputs))
    print(header_line)
    for i in range(num_combinations):
        row_values = []
        for j in range(num_inputs):
            if (i >> j) & 1:
                row_values.append("1")
            else:
                row_values.append("0")
        print(" ".join(row_values))
if __name__ == '__main__':
    sample_inputs = [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1)
    ]
    print_truth_table(sample_inputs)