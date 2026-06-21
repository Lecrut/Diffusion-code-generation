def find_maximum(numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty")
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

if __name__ == '__main__':
    sample_numbers = [15, 8, 42, 3, 99, 27]
    maximum_value = find_maximum(sample_numbers)
    print(maximum_value)