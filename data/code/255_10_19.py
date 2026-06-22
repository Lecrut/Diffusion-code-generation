def find_max_value(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
    return max_value
if __name__ == '__main__':
    sample_numbers = [3, 15, -2, 7, 42, -8, 0]
    result = find_max_value(sample_numbers)
    print(result)