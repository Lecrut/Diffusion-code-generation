def get_element_at_index(lst, index):
    if not isinstance(lst, list):
        raise TypeError('The first argument must be a list.')
    if not isinstance(index, int):
        raise TypeError('The index must be an integer.')
    if index < 0:
        index = len(lst) + index
    if index < 0 or index >= len(lst):
        raise IndexError('Index out of range.')
    return lst[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_element_at_index(sample_list, 2))
    print(get_element_at_index(sample_list, -1))
    try:
        print(get_element_at_index(sample_list, 10))
    except IndexError as e:
        print(e)