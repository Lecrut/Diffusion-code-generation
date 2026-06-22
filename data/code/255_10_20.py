def find_max_value(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value
if __name__ == '__main__':
    sample_numbers = [10, 5, 22, 8, 30, 1]
    print(find_max_value(sample_numbers))
    empty_list = []
    print(find_max_value(empty_list))
    all_negative_numbers = [-10, -5, -22, -8, -30, -1]
    print(find_max_value(all_negative_numbers))