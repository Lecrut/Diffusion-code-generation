def check_consistency(input1, input2, expected_output):
    actual_output = input1 and input2
    return actual_output == expected_output
if __name__ == '__main__':
    test_cases = [
        (0, 0, 0),
        (0, 1, 0),
        (1, 0, 0),
        (1, 1, 1),
        (0, 0, 1),
        (1, 0, 0),
        (0, 1, 0),
        (1, 1, 1)
    ]
    all_consistent = True
    for i1, i2, expected in test_cases:
        result = check_consistency(i1, i2, expected)
        if not result:
            all_consistent = False
            print(f"Inconsistent: Inputs ({i1}, {i2}), Expected ({expected}), Actual ({i1} and {i2})")
    if all_consistent:
        print("All test cases passed consistency check.")
    else:
        print("Some test cases failed consistency check.")