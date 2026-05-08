def print_truth_table(input_combinations):
    if not input_combinations:
        return
    num_inputs = len(input_combinations[0])
    num_rows = len(input_combinations)
    header = "Input | " + " | ".join(str(i) for i in range(num_inputs)) + " | Output\n"
    separator = "-" * len(header)
    print(header)
    print(separator)
    for i in range(num_rows):
        row_output = []
        for j in range(num_inputs):
            row_output.append(str(input_combinations[i][j]))
        row_output.append(" | ")
        print(" | ".join(row_output))
if __name__ == '__main__':
    sample_data = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]
    print_truth_table(sample_data)