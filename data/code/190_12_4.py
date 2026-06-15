def exists_set_method(element, data_list):
    data_set = set(data_list)
    return element in data_set
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    element1 = 8
    result1 = exists_set_method(element1, list1)
    print(f"List: {list1}, Element: {element1}, Exists: {result1}")
    list2 = [10, 20, 30, 40]
    element2 = 50
    result2 = exists_set_method(element2, list2)
    print(f"List: {list2}, Element: {element2}, Exists: {result2}")
    list3 = ['a', 'b', 'c']
    element3 = 'd'
    result3 = exists_set_method(element3, list3)
    print(f"List: {list3}, Element: {element3}, Exists: {result3}")