def validate_input(numbers):
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("All elements must be integers or floats")
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")

def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    sample_values = [5, 10, 15, 20]
    validate_input(sample_values)
    mean = calculate_mean(sample_values)
    print(mean)