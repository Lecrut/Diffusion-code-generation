def validate_input(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    for value in data:
        if not isinstance(value, (int, float)):
            raise TypeError("All elements must be numbers")

def calculate_range(numbers):
    validate_input(numbers)
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [34, 12, 90, 56, 23]
    print(calculate_range(sample_values))