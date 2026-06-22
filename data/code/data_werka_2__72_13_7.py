def compare_elements_at_indices(list1, list2, indices):
    if not isinstance(list1, (list, tuple)):
        raise ValueError("list1 must be a list or tuple")
    if not isinstance(list2, (list, tuple)):
        raise ValueError("list2 must be a list or tuple")
    if not isinstance(indices, (list, tuple)):
        raise ValueError("indices must be a list or tuple")
    
    len1 = len(list1)
    len2 = len(list2)
    results = []
    
    for idx in indices:
        if not isinstance(idx, int):
            results.append(False)
            continue
        try:
            val1 = list1[idx]
            val2 = list2[idx]
            results.append(val1 == val2)
        except (IndexError, TypeError):
            results.append(False)
            
    return results

if __name__ == '__main__':
    list_a = [10, 20, 30, 40, 50]
    list_b = [10, 25, 30, 45, 60]
    indices = [0, 1, 2, 3, 4, 5, -1]
    print(compare_elements_at_indices(list_a, list_b, indices))