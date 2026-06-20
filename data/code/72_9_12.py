def compare_elements(lst, index1, index2):
    if not lst:
        return 'Empty list'
    element1 = lst[index1] if index1 < len(lst) else None
    element2 = lst[index2] if index2 < len(lst) else None
    if element1 is None and element2 is None:
        return 'Both elements out of bounds'
    if element1 is None:
        return f'Element at index {index1} out of bounds'
    if element2 is None:
        return f'Element at index {index2} out of bounds'
    if element1 == element2:
        return 'Equal'
    elif element1 > element2:
        return 'Greater than'
    else:
        return 'Less than'
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(compare_elements(sample_list, 2, 4))
    print(compare_elements(sample_list, 1, 3))
    print(compare_elements(sample_list, 0, 5))
    print(compare_elements([], 2, 4))