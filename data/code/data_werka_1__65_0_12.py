def validate_index(lst, index):
    if not isinstance(lst, list):
        raise TypeError('The first argument must be a list.')
    if not isinstance(index, int):
        raise TypeError('The second argument must be an integer.')
    if index < 0 or index >= len(lst):
        return False
    return True

def get_element_by_position(lst, index):
    if validate_index(lst, index):
        return lst[index]
    else:
        return None
if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date']
    valid_index = 2
    invalid_index = 10
    element_valid = get_element_by_position(sample_list, valid_index)
    print(element_valid)
    element_invalid = get_element_by_position(sample_list, invalid_index)
    print(element_invalid)