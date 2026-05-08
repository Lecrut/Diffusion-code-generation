def print_truth_table(input_combinations):
    if not input_combinations:
        return
    num_inputs = len(input_combinations)
    num_rows = 2**num_inputs
    header = "Input | " + " | ".join(str(i) for i in range(num_rows))
    print(header)
    print("-" * len(header))
    for i in range(num_rows):
        row_values = []
        for j in range(num_inputs):
            if (i >> j) & 1:
                row_values.append("1")
            else:
                row_values.append("0")
        print(f"{' | '.join(map(str, input_combinations[j]))} |", end="")
        print(" ".join(row_values))
        print()
if __name__ == '__main__':
    sample_inputs = [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ]
    print_truth_table(sample_inputs)