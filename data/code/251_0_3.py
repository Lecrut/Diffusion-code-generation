def determine_the_largest_number_present_transform(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

if __name__ == '__main__':
    sample_numbers = [10, 45, 23, 78, 56]
    print(determine_the_largest_number_present_transform(sample_numbers))