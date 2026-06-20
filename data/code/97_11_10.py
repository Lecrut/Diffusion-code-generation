def generate_truth_table(input_combinations):
    return [[a or b for a, b in zip(inputs, inputs[1:])] for inputs in input_combinations]

if __name__ == '__main__':
    sample_inputs = [[True, False], [False, True]]
    print(generate_truth_table(sample_inputs))