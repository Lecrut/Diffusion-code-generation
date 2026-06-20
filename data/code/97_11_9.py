def generate_truth_table(inputs):
    results = []
    for input_combination in inputs:
        a, b = input_combination
        result = (a or b)
        results.append(result)
    return results

if __name__ == '__main__':
    sample_inputs = [(True, True), (True, False), (False, True), (False, False)]
    print(generate_truth_table(sample_inputs))