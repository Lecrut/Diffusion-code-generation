def validate_input(data):
    if not all(isinstance(item, (int, float)) for item in data):
        raise ValueError("All elements must be numeric")

def calculate_average(numbers):
    validate_input(numbers)
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    print(calculate_average(sample_numbers))