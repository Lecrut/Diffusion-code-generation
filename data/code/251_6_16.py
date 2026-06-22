def determine_the_largest_number_present_convert_all(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_data = [10, 5, 20, 3, 15, 25]
    largest_number = determine_the_largest_number_present_convert_all(sample_data)
    print(largest_number)
    sample_data_2 = [50, 10, 40, 20, 30]
    largest_number_2 = determine_the_largest_number_present_convert_all(sample_data_2)
    print(largest_number_2)