def validate_numbers(numbers):
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list of numbers")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the list must be integers or floats")

def calculate_average(numbers):
    validate_numbers(numbers)
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    average = calculate_average(sample_data)
    print(f"The average of {sample_data} is: {average}")