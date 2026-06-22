def validate_numbers(numbers):
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("All elements must be numbers")
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")

def calculate_mean(numbers):
    validate_numbers(numbers)
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [5, 10, 15, 20]
    print(calculate_mean(sample_values))