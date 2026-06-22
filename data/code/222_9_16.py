def find_min(numbers):
    return min(numbers)

if __name__ == '__main__':
    test_cases = [
        ([3, 1, 4, 1, 5, 9], 1),
        ([10, 22, -5, 0, 3, 17], -5),
        ([100, 200, 300], 100),
        ([-1, -2, -3, -4, -5], -5)
    ]

    for i, (numbers, expected) in enumerate(test_cases):
        result = find_min(numbers)
        print(f"Test case {i+1}: {'Passed' if result == expected else 'Failed'}")
        print(f"Input: {numbers}, Expected: {expected}, Got: {result}")