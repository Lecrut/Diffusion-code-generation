def get_element_at_index(lst, index):
    if not isinstance(lst, list):
        raise TypeError('The first argument must be a list.')
    if not isinstance(index, int):
        raise TypeError('The index must be an integer.')
    LIST_LENGTH = len(lst)
    if index < 0:
        index += LIST_LENGTH
    if index < 0 or index >= LIST_LENGTH:
        raise IndexError('Index out of range.')
    return lst[index]
if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    try:
        print(get_element_at_index(sample_list, 1))
        print(get_element_at_index(sample_list, -2))
        print(get_element_at_index(sample_list, 5))
    except (TypeError, IndexError) as e:
        print(e)