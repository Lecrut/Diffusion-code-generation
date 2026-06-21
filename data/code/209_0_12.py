import statistics

def validate_input(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the list must be numbers.")
    if len(numbers) == 0:
        raise ValueError("The list cannot be empty.")

def calculate_average(numbers):
    validate_input(numbers)
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    average = calculate_average(sample_values)
    print(average)