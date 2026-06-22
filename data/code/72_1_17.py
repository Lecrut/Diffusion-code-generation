def compare_elements_at_index(list1, list2, index):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Inputs must be lists")
    if not isinstance(index, int):
        raise ValueError("Index must be an integer")
    if index < 0 or index >= len(list1) or index < 0 or index >= len(list2):
        raise ValueError("Index out of range for one or both lists")
    
    elem1 = list1[index]
    elem2 = list2[index]
    
    if elem1 > elem2:
        return (1, elem1, elem2)
    elif elem1 < elem2:
        return (-1, elem1, elem2)
    else:
        return (0, elem1, elem2)

if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [10, 15, 35]
    idx = 1
    result = compare_elements_at_index(list_a, list_b, idx)
    print(result)