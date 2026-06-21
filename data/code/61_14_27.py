def get_element_at_index(lst, index):
    if not isinstance(lst, list):
        raise TypeError('The first argument must be a list.')
    if not isinstance(index, int):
        raise TypeError('The index must be an integer.')
    try:
        return lst[index]
    except IndexError:
        return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_element_at_index(sample_list, 2))
    print(get_element_at_index(sample_list, -1))
    print(get_element_at_index(sample_list, 5))
    print(get_element_at_index(sample_list, -6))