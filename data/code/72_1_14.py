def compare_elements(list1, list2, index):
    if index < len(list1) and index < len(list2):
        element1 = list1[index]
        element2 = list2[index]
        if element1 > element2:
            return (element1, 'greater than', element2)
        elif element1 < element2:
            return (element1, 'less than', element2)
        else:
            return (element1, 'equal to', element2)
    else:
        return ('Index out of range')

if __name__ == '__main__':
    list1 = [10, 20, 30, 40]
    list2 = [5, 25, 30, 45]
    index = 2
    result = compare_elements(list1, list2, index)
    print(result)