def check_consistency(input_a, input_b, output):
    expected_output = input_a and input_b
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
    for a, b, out in test_cases:
        result = check_consistency(a, b, out)
        print(f"Inputs: a={a}, b={b}, Output: {out}, Consistent: {result}")