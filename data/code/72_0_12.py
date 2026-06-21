def compare_elements(list1, list2, index):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Inputs must be lists")
    if not isinstance(index, int):
        raise ValueError("Index must be an integer")
    
    element1 = None
    element2 = None
    
    if 0 <= index < len(list1):
        element1 = list1[index]
    
    if 0 <= index < len(list2):
        element2 = list2[index]
        
    return element1, element2

if __name__ == '__main__':
    source_a = [1, 2, 3, 4, 5]
    source_b = [10, 20, 30, 40, 50]
    target_index = 3
    val_a, val_b = compare_elements(source_a, source_b, target_index)
    print(f"{val_a}, {val_b}")
    
    short_list = [100]
    val_c, val_d = compare_elements(source_a, short_list, 4)
    print(f"{val_c}, {val_d}")