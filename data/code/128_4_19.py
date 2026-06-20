def contains_negative_value(numbers):
    return any(num < 0 for num in numbers)

if __name__ == '__main__':
    test_cases = [
        [10, -5, 0, -100],
        [-2, 3.14, 7],
        [0, 1, 2],
        [-1.5, 42],
        []
    ]
    for case in test_cases:
        result = contains_negative_value(case)
        print(f"Test case {case}: {'Contains negative value' if result else 'Does not contain negative value'}")