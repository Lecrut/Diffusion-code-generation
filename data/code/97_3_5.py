def print_truth_table(input_combinations):
    if not input_combinations:
        return
    num_inputs = len(input_combinations[0])
    num_combinations = len(input_combinations)
    header = "Input | " + " | ".join(str(i) for i in range(num_inputs)) + " | Output\n"
    separator = "-" * (len(header) - 1)
    print(header)
    print(separator)
    for i in range(num_combinations):
        row = f"{i} | "
        for j in range(num_inputs):
            row += str(input_combinations[i][j]) + " | "
        print(row + " " + str(input_combinations[i][num_inputs - 1]))
if __name__ == '__main__':
    sample_inputs = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]
    print_truth_table(sample_inputs)