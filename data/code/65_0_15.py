def get_element_by_position(lst, index):
    if not isinstance(lst, list) or not isinstance(index, int):
        return None
    try:
        return lst[index]
    except IndexError:
        return None
if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date']
    valid_index = 2
    invalid_index = 5
    print(get_element_by_position(sample_list, valid_index))
    print(get_element_by_position(sample_list, invalid_index))