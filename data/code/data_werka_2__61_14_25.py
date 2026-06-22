def get_element_at_index(lst, index):
    if not isinstance(lst, list):
        raise TypeError('The first argument must be a list.')
    if not isinstance(index, int):
        raise TypeError('The index must be an integer.')
    
    LIST_LENGTH = len(lst)
    
    if index < 0:
        adjusted_index = LIST_LENGTH + index
    else:
        adjusted_index = index
    
    if adjusted_index < 0 or adjusted_index >= LIST_LENGTH:
        raise IndexError('Index out of range.')
    
    return lst[adjusted_index]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    try:
        print(get_element_at_index(sample_list, 1))
        print(get_element_at_index(sample_list, -3))
        print(get_element_at_index(sample_list, 7))
    except (TypeError, IndexError) as e:
        print(e)