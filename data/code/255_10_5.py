def find_max_value(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
    return max_value
if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(find_max_value(sample_values))
    empty_list = []
    print(find_max_value(empty_list))
    negative_numbers = [-1, -3, -2, -4]
    print(find_max_value(negative_numbers))