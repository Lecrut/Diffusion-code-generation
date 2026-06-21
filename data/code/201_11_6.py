def validate_numbers(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Input must be a list of numbers")

def calculate_average(numbers):
    validate_numbers(numbers)
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(f"The average of {sample_data} is: {calculate_average(sample_data)}")