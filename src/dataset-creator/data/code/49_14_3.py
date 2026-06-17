def check_positive_result(value):
    return isinstance(value, (int, float)) and value > 0
if __name__ == '__main__':
    test_cases = [5, -3.7, 0, "12", True]
    for case in test_cases:
        result = check_positive_result(case)
        print(f"Input {case}: Positive? {result}")
assert check_positive_result(5.5) is True, "Float positive should be true"
assert check_positive_result(-2) is False, "Int negative should be false"
assert check_positive_result(0) is False, "Zero should not be considered positive"
try:
    assert check_positive_result("10") is False, "String input should return false due to type mismatch"
except AssertionError as e:
    print(f"Test failed for string input: {e}")
print("\nAll assertions passed successfully.")