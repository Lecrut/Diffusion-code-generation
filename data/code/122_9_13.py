from decimal import Decimal

def validate_input(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("All elements must be int or float")

def calculate_average(numbers):
    validate_input(numbers)
    total = Decimal(0)
    count = 0
    for number in numbers:
        total += Decimal(str(number))
        count += 1
    return total / Decimal(count)

if __name__ == '__main__':
    sample_numbers = [3, 5.5, 2, 8.75]
    average = calculate_average(sample_numbers)
    print(average)