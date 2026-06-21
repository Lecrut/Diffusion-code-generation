import statistics

def validate_numbers(numbers):
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list of numbers")
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("All elements in the list must be integers or floats")

def calculate_average(numbers):
    validate_numbers(numbers)
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    print(f"Average of {sample_numbers}: {calculate_average(sample_numbers)}")