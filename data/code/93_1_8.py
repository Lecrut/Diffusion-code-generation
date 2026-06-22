def are_both_false(a, b):
    FALSE_CONSTANT = False
    return a is FALSE_CONSTANT and b is FALSE_CONSTANT

if __name__ == '__main__':
    test_cases = [
        (False, False),
        (False, True),
        (True, False),
        (True, True),
    ]
    for x, y in test_cases:
        print(are_both_false(x, y))