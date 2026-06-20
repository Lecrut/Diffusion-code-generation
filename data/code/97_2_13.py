def print_truth_table(input_combinations):
    headers = [f"Input {i+1}" for i in range(len(input_combinations[0]))] + ["Output"]
    print(" | ".join(headers))
    print("-" * (len(headers) - 1) * len(headers))

    for combination in input_combinations:
        row = " | ".join([str(val) for val in combination])
        print(row)

if __name__ == '__main__':
    sample_inputs = [
        [True, False],
        [False, True],
        [True, True]
    ]
    print_truth_table(sample_inputs)