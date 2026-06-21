def validate_input(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be integers or floats")

def calculate_sum(numbers):
    return sum(numbers)

if __name__ == '__main__':
    sample_values = [10, 20.5, 30, 42]
    validate_input(sample_values)
    result = calculate_sum(sample_values)
    print(f"The total sum is: {result}")