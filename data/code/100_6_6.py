def check_consistency(input_a, input_b, output):
    expected_output = input_a & input_b
    return expected_output == output
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
            all_consistent = False
            print(f"Inconsistent: a={a}, b={b}, output={out}")
            break
    if all_consistent:
        print("All test cases passed consistency check.")
    else:
        print("Some test cases failed consistency check.")