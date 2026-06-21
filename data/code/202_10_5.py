def get_largest_number(numbers):
    if not numbers:
        return None
    return max(numbers)

if __name__ == '__main__':
    test_cases = [
        [10, 5, 22, 8, 3],
        [-1, -5, -22, -8, -3],
        [3.5, 2.1, 4.8, 1.9, 5.2],
        [],
    ]
    
    for i, test_case in enumerate(test_cases):
        result = get_largest_number(test_case)
        print(f"Test case {i+1}: {test_case} -> Largest number: {result}")