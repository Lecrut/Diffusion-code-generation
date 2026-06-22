def validate_numbers(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be numbers")

def determine_the_largest_number_present_transform(numbers):
    validate_numbers(numbers)
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

if __name__ == '__main__':
    sample_numbers = [15, 22, 7, 99, 3, 87]
    print(determine_the_largest_number_present_transform(sample_numbers))