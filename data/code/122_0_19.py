import statistics

def validate_numbers(numbers):
    if not numbers:
        return None
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements in the list must be numbers")
    return True

def calculate_average(numbers):
    if validate_numbers(numbers) is None:
        return None
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    print(calculate_average(sample_numbers))