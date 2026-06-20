def print_truth_table(input_combinations):
    headers = input_combinations[0].keys()
    values = list(zip(*input_combinations))

    for header in headers:
        print(f"{header:<10}", end="")
    print()

    for row in zip(*values):
        for value in row:
            print(f"{value:<10}", end="")
        print()

if __name__ == '__main__':
    sample_inputs = [
        {'A': True, 'B': False},
        {'A': False, 'B': True},
        {'A': True, 'B': True}
    ]
    print_truth_table(sample_inputs)