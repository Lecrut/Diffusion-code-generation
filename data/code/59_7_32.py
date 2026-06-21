def find_middle_item(numbers):
    if not isinstance(numbers, list):
        raise ValueError('Input must be a list')
    if len(numbers) == 0:
        raise ValueError('The list cannot be empty')

    def is_valid_list(lst):
        return all((isinstance(x, (int, float)) for x in lst))
    if not is_valid_list(numbers):
        raise ValueError('All elements in the list must be numbers')
    middle_index = len(numbers) // 2
    return numbers[middle_index]
if __name__ == '__main__':
    sample_list_odd = [1, 3, 5, 7, 9]
    sample_list_even = [2, 4, 6, 8, 10, 12]
    print(find_middle_item(sample_list_odd))
    print(find_middle_item(sample_list_even))