def has_truthy_elements(sequence):
    if not isinstance(sequence, (list, tuple, set, dict)):
        raise ValueError("Expected a list, tuple, set, or dict")
    if isinstance(sequence, dict):
        return any(sequence.values())
    return any(sequence)

if __name__ == '__main__':
    test_cases = [
        [0, 0, 0],
        [False, None, 0, "a"],
        [],
        (0, 0, 0),
        {0: False, 1: 0},
        {0: False, 1: True}
    ]
    for case in test_cases:
        print(has_truthy_elements(case))