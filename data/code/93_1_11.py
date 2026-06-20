def are_both_false(a, b):
    result = not a and not b
    return result

if __name__ == '__main__':
    test_cases = [
        (False, False),
        (True, False),
        (False, True),
        (True, True)
    ]
    for inputs in test_cases:
        print(f"are_both_false{inputs}: {are_both_false(*inputs)}")