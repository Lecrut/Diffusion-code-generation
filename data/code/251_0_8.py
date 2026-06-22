def find_largest_number(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
    return max_value

def validate_input(numbers):
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list of numbers")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the list must be numbers")

def determine_the_largest_number_present_transform(numbers):
    validate_input(numbers)
    return find_largest_number(numbers)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 8, 2]
    print(determine_the_largest_number_present_transform(sample_numbers))