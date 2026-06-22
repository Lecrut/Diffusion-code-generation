def validate_input(combinations):
    if not isinstance(combinations, (list, tuple)):
        raise ValueError("Input must be a list or tuple of combinations")
    for combo in combinations:
        if not isinstance(combo, (list, tuple)):
            raise ValueError("Each combination must be a list or tuple")
        if len(combo) != 2:
            raise ValueError("Each combination must have exactly two elements")
        for val in combo:
            if not isinstance(val, bool):
                raise ValueError("Each element must be a boolean")
    return True

def compute_or_truth_table(combinations):
    validate_input(combinations)
    table = []
    for a, b in combinations:
        table.append([a, b, a or b])
    return table

if __name__ == '__main__':
    inputs = [[True, False], [False, True], [True, True], [False, False]]
    result = compute_or_truth_table(inputs)
    print(result)