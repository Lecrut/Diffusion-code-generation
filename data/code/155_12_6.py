def validate_input(input_list):
    if not all(isinstance(item, (int, float)) for item in input_list):
        raise ValueError("All elements must be numbers")

def calculate_sum(numbers):
    return sum(numbers)

if __name__ == '__main__':
    sample_values = [10, 20.5, 30, 42]
    validate_input(sample_values)
    result = calculate_sum(sample_values)
    print(f"The total sum is: {result}")