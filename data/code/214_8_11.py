def find_minimum(numbers):
    if not numbers:
        raise ValueError('Input list cannot be empty')
    current_min = numbers[0]
    for number in numbers:
        if number < current_min:
            current_min = number
    return current_min
if __name__ == '__main__':
    sample_list = [4, 9, -3, 15, 2, 8]
    min_value = find_minimum(sample_list)
    print(min_value)