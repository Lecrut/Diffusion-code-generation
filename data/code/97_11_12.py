def generate_truth_table(input_combinations):
    return [[x or y for x, y in zip(inputs, inputs)] for inputs in input_combinations]

if __name__ == '__main__':
    sample_inputs = [[True, False], [False, True]]
    print(generate_truth_table(sample_inputs))