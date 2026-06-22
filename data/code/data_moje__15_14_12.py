def get_second_to_last_item(lst):
    if not isinstance(lst, list):
        raise TypeError('Input must be a list')
    if len(lst) < 2:
        raise IndexError('List must have at least 2 elements')
    return lst[-2]
if __name__ == '__main__':
    sample_lists = [[1, 2, 3, 4, 5], ['apple', 'banana', 'cherry', 'date'], [10, 20], [True, False, True, False]]
    for sample_list in sample_lists:
        result = get_second_to_last_item(sample_list)
        print(result)