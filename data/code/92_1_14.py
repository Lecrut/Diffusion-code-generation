TRUE_VALUE = True
FALSE_VALUE = False
INVERT_MAP = {TRUE_VALUE: FALSE_VALUE, FALSE_VALUE: TRUE_VALUE}

def find_opposite_truth(truth: bool) -> bool:
    if truth not in INVERT_MAP:
        raise ValueError("Input must be a boolean")
    return INVERT_MAP[truth]

if __name__ == '__main__':
    test_input = True
    output = find_opposite_truth(test_input)
    print(output)
    test_input = False
    output = find_opposite_truth(test_input)
    print(output)