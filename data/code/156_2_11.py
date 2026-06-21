def validate_numbers(numbers):
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("All elements must be integers or floats")
    if len(numbers) == 0:
        return []
    return numbers

def calculate_average(numbers):
    validated_numbers = validate_numbers(numbers)
    return sum(validated_numbers) / len(validated_numbers)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    average = calculate_average(sample_list)
    print(average)