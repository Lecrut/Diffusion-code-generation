def validate_input(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the list must be floats or integers.")
    return numbers

def calculate_float_sum(numbers):
    total = 0.0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_list = [1.5, 2.75, 3.0, -4.2, 0.1]
    validated_numbers = validate_input(sample_list)
    result = calculate_float_sum(validated_numbers)
    print(result)