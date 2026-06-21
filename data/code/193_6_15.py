def validate_data(data):
    if not all(isinstance(item, (int, float)) for item in data):
        raise ValueError("All elements in the list must be integers or floats")

def sum_mixed_numbers(numbers):
    validate_data(numbers)
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_values = [1, 2.5, 3, 4.75]
    print(sum_mixed_numbers(sample_values))