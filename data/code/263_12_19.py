def common_elements(list1, list2):
    return [element for element in set(list1) if element in list2]

if __name__ == '__main__':
    result = common_elements([1, 2, 3, 4], [2, 3, 5, 6])
    print(result)