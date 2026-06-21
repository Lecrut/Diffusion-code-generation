def validate_numbers(numbers):
    if not numbers:
        raise ValueError("The list must contain at least one number.")
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements in the list must be numbers.")

def calculate_average(numbers):
    validate_numbers(numbers)
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    sample_numbers = [5, 10, 15, 20, 25]
    avg = calculate_average(sample_numbers)
    print(avg)