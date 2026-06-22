def find_minimum(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    minimum_value = numbers[0]
    for number in numbers[1:]:
        if number < minimum_value:
            minimum_value = number
    return minimum_value

if __name__ == '__main__':
    sample_list = [5, 2, 9, 1, 7]
    result = find_minimum(sample_list)
    print(result)