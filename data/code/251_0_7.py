def determine_the_largest_number_present_transform(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

if __name__ == '__main__':
    sample_numbers = [42, 99, 56, 87, 33, 101]
    largest_number = determine_the_largest_number_present_transform(sample_numbers)
    print(largest_number)