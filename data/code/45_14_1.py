def find_minimum(numbers):
    if not isinstance(numbers, list):
        raise TypeError('Input must be a list')
    if len(numbers) == 0:
        raise ValueError('List cannot be empty')
    for item in numbers:
        if not isinstance(item, (int, float)):
            raise TypeError('All elements must be numeric')
    min_value = numbers[0]
    for number in numbers[1:]:
        if number < min_value:
            min_value = number
    return min_value
if __name__ == '__main__':
    sample_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = find_minimum(sample_numbers)
    print(result)