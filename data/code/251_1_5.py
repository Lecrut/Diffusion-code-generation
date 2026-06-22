def determine_the_largest_number_present_validate(numbers):
    if not isinstance(numbers, list) or not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Input must be a list of numbers")
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")
    return max(numbers)

def find_largest(data):
    return determine_the_largest_number_present_validate(data)

if __name__ == '__main__':
    sample_data = [15, 25, 35, 45, 55]
    largest_number = find_largest(sample_data)
    print(largest_number)