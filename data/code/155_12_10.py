def validate_numbers(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be numbers")

def calculate_sum(numbers):
    validate_numbers(numbers)
    return sum(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 35, 42]
    result = calculate_sum(sample_values)
    print(f"The total sum is: {result}")