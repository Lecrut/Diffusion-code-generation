def find_min(numbers):
    if not numbers:
        return None
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value

if __name__ == '__main__':
    test_cases = [
        ([3, 1, 4, 1, 5, 9, 2, 6], 1),
        ([7, -2, 0, 8, 5], -2),
        ([100, 200, 300], 100),
        ([], None),
        ([-1, -1, -1], -1)
    ]
    
    for i, (numbers, expected) in enumerate(test_cases):
        result = find_min(numbers)
        print(f"Test case {i+1}: {'Passed' if result == expected else 'Failed'}")