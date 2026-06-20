def generate_truth_table(input_combinations):
    return [[x or y for y in [False, True]] for x in input_combinations]

if __name__ == '__main__':
    sample_inputs = [[True, False], [False, True]]
    print(generate_truth_table(sample_inputs))