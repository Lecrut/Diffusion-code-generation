def _validate_index(length, index):
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if index < 0:
        raise IndexError("Index must be non-negative")
    if index >= length:
        raise IndexError("Index out of range for list")

def _get_element_or_none(lst, index):
    try:
        return lst[index]
    except (IndexError, TypeError):
        return None

def compare_elements_at_index(list1, list2, index):
    len1 = len(list1)
    len2 = len(list2)
    
    _validate_index(len1, index)
    _validate_index(len2, index)
    
    val1 = list1[index]
    val2 = list2[index]
    
    if val1 > val2:
        return (1, val1, val2)
    elif val1 < val2:
        return (-1, val1, val2)
    else:
        return (0, val1, val2)

if __name__ == '__main__':
    list_a = [10, 20, 30, 40]
    list_b = [15, 20, 35, 40]
    idx = 1
    result = compare_elements_at_index(list_a, list_b, idx)
    print(result)
    
    list_c = [5, 10, 15]
    list_d = [5, 12, 15]
    idx2 = 1
    result2 = compare_elements_at_index(list_c, list_d, idx2)
    print(result2)
    
    list_e = [1, 2, 3]
    list_f = [1, 2, 3]
    idx3 = 2
    result3 = compare_elements_at_index(list_e, list_f, idx3)
    print(result3)