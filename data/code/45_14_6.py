def find_minimum(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    min_value = numbers[0]
    for number in numbers[1:]:
        if number < min_value:
            min_value = number
    return min_value

if __name__ == '__main__':
    sample_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = find_minimum(sample_numbers)
    print(result)