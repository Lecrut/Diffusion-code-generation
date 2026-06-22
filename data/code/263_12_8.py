def common_elements(list1, list2):
    return [element for element in list1 if element in list2]

if __name__ == '__main__':
    print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
    print(common_elements(['apple', 'banana'], ['banana', 'cherry']))
    print(common_elements([True, False], [False, True]))