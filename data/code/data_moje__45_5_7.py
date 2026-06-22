def get_minimum_value(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if len(numbers) == 0:
        raise ValueError("List cannot be empty.")
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_list = [5, 3, 9, 1, 7]
    result = get_minimum_value(sample_list)
    print(result)
    invalid_input = "not a list"
    try:
        get_minimum_value(invalid_input)
    except TypeError as e:
        print(e)
    empty_list = []
    try:
        get_minimum_value(empty_list)
    except ValueError as e:
        print(e)