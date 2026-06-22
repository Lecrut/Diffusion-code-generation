def determine_the_largest_number_present_calculate(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    largest = max(numbers)
    return largest

if __name__ == '__main__':
    sample_data = [42, 10, 99, 5, 123, 78]
    try:
        result = determine_the_largest_number_present_calculate(sample_data)
        print(result)
    except ValueError as e:
        print(e)