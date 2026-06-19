def find_middle_item(numbers):
    if not isinstance(numbers, list):
        raise TypeError('Input must be a list.')
    if len(numbers) == 0:
        raise ValueError('List cannot be empty.')
    middle_index = (len(numbers) - 1) // 2
    return numbers[middle_index]
if __name__ == '__main__':
    sample_list_odd = [1, 3, 5, 7, 9]
    sample_list_even = [2, 4, 6, 8, 10, 12]
    try:
        print(find_middle_item(sample_list_odd))
        print(find_middle_item(sample_list_even))
    except (TypeError, ValueError) as e:
        print(e)