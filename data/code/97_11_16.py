def generate_truth_table(inputs):
    results = []
    for combo in inputs:
        a, b = combo
        result = a or b
        results.append((a, b, result))
    return results

if __name__ == '__main__':
    sample_inputs = [[True, False], [False, True], [True, True], [False, False]]
    truth_table = generate_truth_table(sample_inputs)
    for entry in truth_table:
        print(f"a={entry[0]}, b={entry[1]}: {entry[2]}")