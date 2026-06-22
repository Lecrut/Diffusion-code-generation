def find_minimum(numbers):
    if not isinstance(numbers, list):
        raise TypeError('Input must be a list')
    if not numbers:
        raise ValueError('List is empty')
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError('All elements must be numbers')
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val
if __name__ == '__main__':
    sample_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = find_minimum(sample_numbers)
    print(result)