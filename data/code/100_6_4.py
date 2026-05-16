def check_consistency(input1, input2, output):
    expected_output = input1 & input2
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
    for i1, i2, o in test_cases:
        result = check_consistency(i1, i2, o)
        print(f"Inputs: {i1}, {i2}, Output: {o}, Consistent: {result}")