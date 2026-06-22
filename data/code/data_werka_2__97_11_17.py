def validate_combinations(combinations):
    if not isinstance(combinations, (list, tuple)):
        raise TypeError("Input must be a list of combinations")
    for i, combo in enumerate(combinations):
        if not isinstance(combo, (list, tuple)):
            raise ValueError(f"Combination at index {i} must be a list or tuple")
        if len(combo) != 2:
            raise ValueError(f"Combination at index {i} must have exactly two elements")
        for j, val in enumerate(combo):
            if not isinstance(val, bool):
                raise ValueError(f"Element at index {j} in combination {i} must be a boolean")
    return combinations

def compute_or_results(combinations):
    validated = validate_combinations(combinations)
    return [
        [a, b, a | b]
        for a, b in validated
    ]

if __name__ == '__main__':
    sample_inputs = [[True, False], [False, True], [True, True], [False, False]]
    truth_table = compute_or_results(sample_inputs)
    print(truth_table)