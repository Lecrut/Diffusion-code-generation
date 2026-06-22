def find_max_value(numbers):
    if not numbers:
        raise ValueError('List cannot be empty')
    max_val = numbers[0]
    for number in numbers[1:]:
        if number > max_val:
            max_val = number
    return max_val
if __name__ == '__main__':
    sample_data = [3, 5, 1, 2, 4]
    print(find_max_value(sample_data))