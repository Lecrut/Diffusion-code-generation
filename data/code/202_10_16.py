def get_largest_number(numbers):
    if not numbers:
        return None
    return max(numbers)

if __name__ == '__main__':
    test_cases = [
        [10, 5, 22, 8, 3],
        [-1, -2, -3, -4, -5],
        [3.14, 2.71, 1.618, 0.577],
        [],
        [42]
    ]
    
    for case in test_cases:
        print(f"Input: {case} -> Output: {get_largest_number(case)}")