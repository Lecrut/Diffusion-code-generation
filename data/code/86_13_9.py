IDENTICAL_BOOLEANS = True

def compare_booleans(a: bool, b: bool) -> bool:
    return a == b
if __name__ == '__main__':
    test_cases = [(True, True), (False, False), (True, False)]
    for inputs in test_cases:
        result = compare_booleans(*inputs)
        print(f'compare_booleans{inputs} -> {result}')