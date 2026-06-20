def is_negative(value):
    return value < 0

if __name__ == '__main__':
    test_values = [1, -2, 3, -4, 5]
    for val in test_values:
        assert is_negative(val) == (val < 0), f"Test Failed: {val} should be {'negative' if val < 0 else 'non-negative'}"
    print("All tests passed")