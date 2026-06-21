def validate_pair(combination):
    if not isinstance(combination, (list, tuple)):
        raise ValueError("Each input must be a list or tuple")
    if len(combination) != 2:
        raise ValueError("Each combination must contain exactly two elements")
    for item in combination:
        if not isinstance(item, bool):
            raise ValueError("All elements must be boolean values")
    return combination

def calculate_or_results(combinations):
    results = []
    for combo in combinations:
        validated = validate_pair(combo)
        val1, val2 = validated
        results.append((val1, val2, val1 or val2))
    return results

if __name__ == '__main__':
    sample_inputs = [
        [True, True],
        [True, False],
        [False, True],
        [False, False]
    ]
    truth_table_data = calculate_or_results(sample_inputs)
    print(truth_table_data)