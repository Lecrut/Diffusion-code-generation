def validate_input(numbers):
    if len(numbers) != 2:
        raise ValueError("Input must be a list of two elements")
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("Both elements must be valid numbers")

def multiply_numbers(numbers):
    validate_input(numbers)
    return numbers[0] * numbers[1]

if __name__ == '__main__':
    sample_values = [8, 6]
    result = multiply_numbers(sample_values)
    print(f"The product of {sample_values[0]} and {sample_values[1]} is: {result}")