def validate_numbers(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("One or more inputs were not valid numbers.")
    return numbers

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    try:
        validated_numbers = validate_numbers(sample_numbers)
        avg = calculate_average(validated_numbers)
        print(avg)
    except ValueError as e:
        print(e)