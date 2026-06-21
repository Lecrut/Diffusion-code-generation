def validate_numbers(numbers):
    if not numbers:
        raise ValueError("Cannot calculate the mean of an empty list")

def calculate_mean(numbers):
    validate_numbers(numbers)
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = (1, 2, 3, 4, 5)
    print(calculate_mean(sample_values))