def is_negative(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be an integer or float")
    return value < 0

if __name__ == '__main__':
    test_values = [1, -2, 3.5, -4.5, "abc", None]
    expected_results = [False, True, False, True, False, False]

    for i, val in enumerate(test_values):
        try:
            result = is_negative(val)
            assert result == expected_results[i], f"Test {i+1} Failed: Expected {expected_results[i]}, Got {result}"
            print(f"Test {i+1} Passed")
        except ValueError as e:
            assert str(e) == "Input must be an integer or float", f"Test {i+1} Failed: {e}"
            print(f"Test {i+1} Passed (Invalid Input)")