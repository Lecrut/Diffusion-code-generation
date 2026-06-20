def are_both_false(a, b):
    return not a and not b

if __name__ == '__main__':
    test_cases = [
        (False, False),
        (True, False),
        (False, True),
        (True, True)
    ]
    for inputs in test_cases:
        result = are_both_false(*inputs)
        print(f"are_both_false{inputs}: {result}")