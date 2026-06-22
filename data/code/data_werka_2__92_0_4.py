TRUE_VALUE = True
FALSE_VALUE = False

def invert_truth(state: bool) -> bool:
    if not isinstance(state, bool):
        raise ValueError("Input must be a boolean type")
    if state is TRUE_VALUE:
        return FALSE_VALUE
    return TRUE_VALUE

if __name__ == '__main__':
    test_cases = [True, False]
    for case in test_cases:
        result = invert_truth(case)
        print(result)