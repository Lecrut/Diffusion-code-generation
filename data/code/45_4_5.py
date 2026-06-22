def find_minimum(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    minimum_value = numbers[0]
    index = 1
    list_length = len(numbers)
    while index < list_length:
        value = numbers[index]
        if value < minimum_value:
            minimum_value = value
        index += 1
    return minimum_value

if __name__ == '__main__':
    sample_data = [45, 12, 88, 3, 99, 21, 7, 56, 30, 4]
    result = find_minimum(sample_data)
    print(result)