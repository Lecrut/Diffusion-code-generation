def get_largest_number(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    return max(numbers)

if __name__ == '__main__':
    try:
        test_cases = [
            [10, 5, 22, 8, 3],
            [-1, -5, -22, -8, -3],
            [3.5, 2.1, 4.8, 1.9],
            [],
            ["a", "b", "c"]
        ]
        for case in test_cases:
            try:
                result = get_largest_number(case)
                print(f"Input: {case}, Largest Number: {result}")
            except ValueError as e:
                print(f"Input: {case}, Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")