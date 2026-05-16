def check_consistency(input_a, input_b, output):
    expected_output = input_a & input_b
    return output == expected_output
if __name__ == '__main__':
    test_cases = [
        (0, 0, 0),
        (0, 1, 0),
        (1, 0, 0),
        (1, 1, 1),
        (0, 0, 1),
        (1, 0, 1),
        (0, 1, 1),
        (1, 1, 0)
    ]
    all_consistent = True
    for a, b, out in test_cases:
        if not check_consistency(a, b, out):
            print(f"Inconsistent: a={a}, b={b}, output={out}")
            all_consistent = False
    if all_consistent:
        print("All test cases are consistent.")
    else:
        print("Some test cases are inconsistent.")