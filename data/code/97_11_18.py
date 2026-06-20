def generate_truth_table(input_combinations):
    truth_table = []
    for combination in input_combinations:
        result = any(combination)
        truth_table.append(result)
    return truth_table

if __name__ == '__main__':
    sample_inputs = [[True, False], [False, True], [True, True], [False, False]]
    print(generate_truth_table(sample_inputs))