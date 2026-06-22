def validate_numbers(numbers):
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("All elements must be integers or floats")
    if len(numbers) == 0:
        raise ValueError("The list cannot be empty")

def determine_the_largest_number_present_transform(numbers):
    validate_numbers(numbers)
    return max(numbers)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 8, 2]
    print(determine_the_largest_number_present_transform(sample_numbers))