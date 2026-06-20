def validate_inputs(combinations):
    if not all(isinstance(item, list) for item in combinations):
        raise ValueError("Input must be a list of lists.")
    for combo in combinations:
        if len(combo) != 2 or not all(isinstance(val, bool) for val in combo):
            raise ValueError("Each sublist must contain exactly two boolean values.")

def generate_and_truth_table(combinations):
    validate_inputs(combinations)
    results = []
    for combo in combinations:
        a, b = combo
        and_result = a and b
        results.append((a, b, and_result))
    return results

if __name__ == '__main__':
    sample_combinations = [
        [True, False],
        [False, True],
        [True, True],
        [False, False]
    ]
    truth_table = generate_and_truth_table(sample_combinations)
    for row in truth_table:
        print(row)