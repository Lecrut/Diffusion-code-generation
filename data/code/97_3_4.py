def print_truth_table(input_combinations):
    if not input_combinations:
        return
    num_inputs = len(input_combinations[0])
    num_combinations = len(input_combinations)
    header = "Input | " + " | ".join(f"C{i}" for i in range(num_inputs))
    print(header)
    print("-" * len(header))
    for i in range(num_combinations):
        row_output = f"C{i}"
        for j in range(num_inputs):
            row_output += f" ({input_combinations[i][j]})"
        print(row_output)
if __name__ == '__main__':
    sample_data = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]
    print_truth_table(sample_data)