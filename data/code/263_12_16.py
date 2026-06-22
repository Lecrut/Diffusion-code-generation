def find_common_elements(list1, list2):
    return [element for element in list1 if element in list2]

if __name__ == '__main__':
    print(find_common_elements([1, 2, 3, 4], [2, 4, 6, 8]))
    print(find_common_elements(['a', 'b', 'c'], ['c', 'd', 'e']))
    print(find_common_elements([True, False], [False, True, True]))