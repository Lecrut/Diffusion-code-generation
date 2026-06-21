def get_largest_number(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Input must be a list of numeric values")
    return max(numbers)

if __name__ == '__main__':
    test_cases = [
        [10, 5, 22, 8, 3],
        [-1, -5, -22, -8, -3],
        [1.5, 2.5, 3.5, 4.5, 5.5],
        [],
        ['a', 'b', 'c'],
        None
    ]
    for i, test_case in enumerate(test_cases):
        try:
            result = get_largest_number(test_case)
            print(f"Test case {i+1}: {result}")
        except ValueError as e:
            print(f"Test case {i+1}: Error - {e}")