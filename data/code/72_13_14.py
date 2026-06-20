def compare_elements_at_indices(list1, list2, indices):
    if not all(isinstance(i, int) for i in indices):
        raise ValueError("All elements in 'indices' must be integers.")
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise TypeError("Both 'list1' and 'list2' must be lists.")
    
    result = []
    for index in indices:
        try:
            if list1[index] == list2[index]:
                result.append(True)
            else:
                result.append(False)
        except IndexError:
            result.append(False)
    
    return result

if __name__ == '__main__':
    print(compare_elements_at_indices([1, 2, 3], [4, 5, 6], [0, 2]))
    print(compare_elements_at_indices(['a', 'b'], ['c', 'd', 'e'], [1, 2]))