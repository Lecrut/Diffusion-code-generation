def find_maximum_value(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    current_max = numbers[0]
    for number in numbers[1:]:
        if number > current_max:
            current_max = number
    return current_max

if __name__ == '__main__':
    sample_numbers = [7, 3, 8, 2, 9, 4]
    max_value = find_maximum_value(sample_numbers)
    print(max_value)