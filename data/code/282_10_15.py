def validate_sequence(numbers):
    if not isinstance(numbers, list) or not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Input must be a list of numbers")

def calculate_sequence_sum(numbers):
    validate_sequence(numbers)
    return sum(numbers)

if __name__ == '__main__':
    sample_data = [1, 5, 10, 15, 20]
    result = calculate_sequence_sum(sample_data)
    print(result)