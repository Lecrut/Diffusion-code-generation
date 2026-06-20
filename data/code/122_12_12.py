def validate_numbers(numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty.")

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    validate_numbers(sample_values)
    average = calculate_average(sample_values)
    print(average)