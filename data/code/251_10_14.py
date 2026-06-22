def determine_the_largest_number_present_calculate(numbers):
    if not numbers:
        raise ValueError("Error: Input list is empty")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_data = [42, 10, 99, 5, 123, 78]
    try:
        print(determine_the_largest_number_present_calculate(sample_data))
    except ValueError as e:
        print(e)