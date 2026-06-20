def compare_elements(list1, list2, index):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError('Both arguments must be lists')
    if not isinstance(index, int):
        raise ValueError('Index must be an integer')
    if index < 0:
        raise IndexError('Index cannot be negative')
    if index >= len(list1) or index >= len(list2):
        raise IndexError('Index out of range for one or both lists')
    return list1[index] <= list2[index]
if __name__ == '__main__':
    result = compare_elements([1, 2, 3], [4, 5, 6], 1)
    print(result)