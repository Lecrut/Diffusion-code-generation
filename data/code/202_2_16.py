def find_greatest_number(numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty")
    greatest = numbers[0]
    for number in numbers[1:]:
        if number > greatest:
            greatest = number
    return greatest

if __name__ == '__main__':
    sample_numbers = [15, 8, 42, 3, 99, 27, 60, 21]
    maximum_value = find_greatest_number(sample_numbers)
    print(maximum_value)