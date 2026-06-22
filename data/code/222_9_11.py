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
        ([3, 1, 4, 1, 5, 9], 1),
        ([10, -2, 0, 5], -2),
        ([7], 7),
        ([], None)
    ]
    
    for i, (numbers, expected) in enumerate(test_cases):
        result = find_min(numbers)
        print(f"Test case {i+1}: {numbers} -> Expected: {expected}, Got: {result}")