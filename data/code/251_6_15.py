def determine_the_largest_number_present_convert_all(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = determine_the_largest_number_present_convert_all(sample_data)
    print(result)