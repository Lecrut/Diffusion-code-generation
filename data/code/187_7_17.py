def find_max_with_index(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    max_index = 0
    for index, value in enumerate(numbers):
        if value > max_value:
            max_value = value
            max_index = index
    return (max_value, max_index)

def validate_input(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, int) for x in numbers):
        raise ValueError("Input must be a list of integers")

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    validate_input(sample_numbers)
    result = find_max_with_index(sample_numbers)
    print(result)