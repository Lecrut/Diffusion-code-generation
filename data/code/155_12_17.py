def validate_input(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers")
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("List elements must be integers or floats")

def sum_numbers(numbers):
    validate_input(numbers)
    return sum(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 35, 42]
    result = sum_numbers(sample_values)
    print(f"The total sum is: {result}")