def perform_operations(numbers):
    if not numbers:
        return 0

    result = numbers[0]
    for number in numbers[1:]:
        if isinstance(number, int) or isinstance(number, float):
            if number > 0:
                result += number
            else:
                result -= abs(number)
        else:
            raise ValueError("All elements must be numbers")

    return result

if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4], 10),
        ([-1, -2, -3, -4], -10),
        ([1, -2, 3, -4], -2)
    ]
    
    for i, (numbers, expected) in enumerate(test_cases):
        result = perform_operations(numbers)
        print(f"Test case {i+1}: {result == expected}")