def find_minimum(numbers):
    if not numbers:
        raise ValueError('Input list cannot be empty')
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8]
    result = find_minimum(sample_list)
    print(result)