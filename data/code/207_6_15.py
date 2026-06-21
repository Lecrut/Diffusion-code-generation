def find_largest(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    largest = next(data)
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
    empty_iterable = iter([])
    for input_list, expected in test_cases:
        try:
            result = find_largest(input_list)
            print(f"Input: {input_list}, Expected: {expected}, Result: {result}")
        except ValueError as e:
            print(e)