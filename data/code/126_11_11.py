def validate_numbers(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements in the list must be integers.")
    return numbers

def find_exact_matches(numbers, target):
    return [num for num in numbers if num == target]

if __name__ == '__main__':
    sample_numbers = validate_numbers([10, 20, 30, 40, 50])
    target_number = 30
    matches = find_exact_matches(sample_numbers, target_number)
    print(matches)