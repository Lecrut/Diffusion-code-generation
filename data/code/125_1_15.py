def validate_numbers(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be numbers")

def perform_operations(numbers):
    result = 0
    for number in numbers:
        if number > 0:
            result += number
        else:
            result -= abs(number)
    return result

if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4], 10),
        ([-1, -2, -3, -4], -10),
        ([1, -2, 3, -4], -2)
    ]
    
    for i, (numbers, expected) in enumerate(test_cases):
        validate_numbers(numbers)
        result = perform_operations(numbers)
        print(f"Test case {i+1}: Result = {result}, Expected = {expected}")