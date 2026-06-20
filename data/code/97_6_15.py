def print_truth_table(input_tuples):
    for P, Q in input_tuples:
        print(f"P: {P}, Q: {Q}")

if __name__ == '__main__':
    sample_values = [(True, True), (True, False), (False, True), (False, False)]
    print_truth_table(sample_values)