def compare_elements(list1, list2, index):
    if index >= len(list1) or index >= len(list2):
        raise IndexError('Index out of range')
    element1 = list1[index]
    element2 = list2[index]
    if element1 > element2:
        return (element1, 'greater than', element2)
    elif element1 < element2:
        return (element1, 'less than', element2)
    else:
        return (element1, 'equal to', element2)
if __name__ == '__main__':
    list1 = [3, 5, 7]
    list2 = [2, 4, 6]
    index = 1
    result = compare_elements(list1, list2, index)
    print(result)