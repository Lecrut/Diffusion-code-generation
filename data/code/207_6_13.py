MAX_VALUE = float('-inf')

def find_largest(data):
    largest = MAX_VALUE
    for item in data:
        if item > largest:
            largest = item
    return largest

if __name__ == '__main__':
    test_cases = [
        ([1, 5, 2, 8, 3], 8),
        ([-10, -5, -20, -1], -1),
        ([5], 5),
        ([-100, -50, -10], -10),
        ([0, 0, 0], 0)
    ]
    for input_list, expected in test_cases:
        result = find_largest(input_list)
        assert result == expected, f"Expected {expected}, got {result}"
        print(f"Input: {input_list}, Expected: {expected}, Result: {result}")