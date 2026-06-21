def validate_numbers(numbers):
    if not all(isinstance(num, float) for num in numbers):
        raise TypeError("All elements in the iterable must be floats")

def calculate_mean(numbers):
    validate_numbers(numbers)
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5]
    print(calculate_mean(sample_values))