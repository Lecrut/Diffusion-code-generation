TRUE_MAP = {True: False}
FALSE_MAP = {False: True}

def invert_boolean(flag: bool) -> bool:
    if not isinstance(flag, bool):
        raise ValueError("Input must be a boolean")
    if flag:
        return TRUE_MAP[True]
    return FALSE_MAP[False]

if __name__ == '__main__':
    test_cases = [True, False]
    for case in test_cases:
        inverted = invert_boolean(case)
        print(inverted)