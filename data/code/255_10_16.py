def find_max_value(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
    return max_value
if __name__ == '__main__':
    sample_values = [10, 5, 22, 8, 30, 1]
    print(find_max_value(sample_values))
    empty_list = []
    print(find_max_value(empty_list))
    negative_numbers = [-5, -3, -10, -1]
    print(find_max_value(negative_numbers))