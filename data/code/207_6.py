def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for item in data[1:]:
        if item > largest:
            largest = item
    return largest
if __name__ == '__main__':
    test_cases = [
        ([1, 5, 2, 8, 3], 8),
        ([-10, -5, -20, -1], -1),
        ([5], 5),
        ([-100, -50, -200], -50),
        ([0, 0, 0], 0)
    ]
    empty_list = []
    for input_list, expected in test_cases:
        result = find_largest(input_list)
        assert result == expected, f"Input: {input_list}, Expected: {expected}, Got: {result}"
        print(f"Test Passed for list: {input_list}")
    try:
        find_largest(empty_list)
        assert False, "Should have raised ValueError for empty list"
    except ValueError as e:
        print(f"Test Passed for empty list: Caught expected error: {e}")
    except Exception as e:
        assert False, f"Caught unexpected exception for empty list: {e}"