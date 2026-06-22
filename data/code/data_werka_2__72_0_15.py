def compare_elements(list1, list2, index):
    if not isinstance(list1, (list, tuple)):
        raise ValueError("list1 must be a list or tuple")
    if not isinstance(list2, (list, tuple)):
        raise ValueError("list2 must be a list or tuple")
    if not isinstance(index, int):
        raise ValueError("index must be an integer")
    
    element1 = None
    element2 = None
    
    try:
        element1 = list1[index]
    except (IndexError, TypeError):
        element1 = "IndexError in list1"
        
    try:
        element2 = list2[index]
    except (IndexError, TypeError):
        element2 = "IndexError in list2"
        
    return element1, element2

if __name__ == '__main__':
    data_a = [1, 2, 3, 4]
    data_b = [10, 20, 30, 40]
    target_index = 2
    val_a, val_b = compare_elements(data_a, data_b, target_index)
    print(f"Element from list 1: {val_a}")
    print(f"Element from list 2: {val_b}")
    
    short_list = [1, 2]
    val_c, val_d = compare_elements(data_a, short_list, 5)
    print(f"Element from list 1 (out of bounds): {val_c}")
    print(f"Element from list 2 (out of bounds): {val_d}")