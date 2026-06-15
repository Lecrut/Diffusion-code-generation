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
        ([-10, -2, -5], -2),
        ([0, 0, 0], 0)
    ]
    print("Running tests for find_largest...")
    for input_list, expected in test_cases:
        try:
            result = find_largest(input_list)
            assert result == expected, f"Input: {input_list}, Expected: {expected}, Got: {result}"
            print(f"Test Passed for {input_list}: Result {result} == Expected {expected}")
        except ValueError as e:
            if len(input_list) == 0 and expected is None:
                print(f"Test Passed for empty list {input_list}: Raised expected error.")
            else:
                print(f"Test Failed for {input_list}: Unexpected error raised: {e}")
        except AssertionError as e:
            print(f"Test Failed for {input_list}: {e}")
    empty_list = []
    try:
        find_largest(empty_list)
        print("Test Failed for empty list: Did not raise ValueError.")
    except ValueError:
        print("Test Passed for empty list: Correctly raised ValueError.")
    except Exception as e:
        print(f"Test Failed for empty list: Raised unexpected exception: {e}")