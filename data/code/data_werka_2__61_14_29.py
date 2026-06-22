def validate_list(lst):
    if not isinstance(lst, list):
        raise TypeError('The first argument must be a list.')

def validate_index(index):
    if not isinstance(index, int):
        raise TypeError('The index must be an integer.')

def adjust_negative_index(lst, index):
    return len(lst) + index

def get_element_at_index(lst, index):
    validate_list(lst)
    validate_index(index)
    
    length = len(lst)
    
    if index < 0:
        index = adjust_negative_index(lst, index)
    
    if index < 0 or index >= length:
        raise IndexError('Index out of range.')
    
    return lst[index]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    try:
        print(get_element_at_index(sample_list, 3))
        print(get_element_at_index(sample_list, -1))
        print(get_element_at_index(sample_list, 5))
    except (TypeError, IndexError) as e:
        print(e)