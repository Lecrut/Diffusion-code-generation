def check_existence_set(element, data_list):
    data_set = set(data_list)
    return element in data_set
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    element1 = 8
    result1 = check_existence_set(element1, list1)
    print(f"List: {list1}, Element: {element1}, Exists: {result1}")
    list2 = ['a', 'b', 'c', 'd']
    element2 = 'e'
    result2 = check_existence_set(element2, list2)
    print(f"List: {list2}, Element: {element2}, Exists: {result2}")
    list3 = [10, 20, 30]
    element3 = 15
    result3 = check_existence_set(element3, list3)
    print(f"List: {list3}, Element: {element3}, Exists: {result3}")