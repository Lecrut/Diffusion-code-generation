import statistics

def validate_numbers(numbers):
    if not numbers:
        raise ValueError("The list must not be empty")
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements in the list must be numbers")

def calculate_average(numbers):
    try:
        validate_numbers(numbers)
        return statistics.mean(numbers)
    except (ValueError, TypeError) as e:
        print(e)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    average = calculate_average(sample_values)
    if average is not None:
        print(average)