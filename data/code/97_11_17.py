def generate_truth_table(input_combinations):
    truth_table = []
    for inputs in input_combinations:
        result = any(inputs)
        truth_table.append(result)
    return truth_table

if __name__ == '__main__':
    sample_inputs = [[True, False], [False, True], [True, True], [False, False]]
    print(generate_truth_table(sample_inputs))