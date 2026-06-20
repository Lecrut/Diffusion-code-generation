def test_or_condition(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError('Both inputs must be boolean values')
    return a or b
if __name__ == '__main__':
    test_cases = [(True, True, True), (True, False, True), (False, True, True), (False, False, False), ('a', True, ValueError), (True, 'b', ValueError)]
    all_passed = True
    for a, b, expected in test_cases:
        try:
            result = test_or_condition(a, b)
            if result != expected:
                print(f'Test failed for a={a}, b={b}. Expected: {expected}, Got: {result}')
                all_passed = False
        except ValueError as e:
            if not isinstance(expected, type(e)):
                print(f'Test failed for a={a}, b={b}. Expected exception of type {type(expected)}, but got {e}')
                all_passed = False
    if all_passed:
        print('All tests passed.')