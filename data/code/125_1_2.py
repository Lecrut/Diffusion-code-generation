def arithmetic_operations(numbers):
    result = 0
    for number in numbers:
        if isinstance(number, (int, float)):
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
        result = arithmetic_operations(numbers)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed: {numbers} -> {result}")