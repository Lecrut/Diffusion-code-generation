def find_minimum(numbers):
    if not numbers:
        raise ValueError('Input list cannot be empty')
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum
if __name__ == '__main__':
    sample_list = [15, 8, 34, 2, 9, 76, 1]
    result = find_minimum(sample_list)
    print(result)