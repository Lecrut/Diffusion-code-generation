def find_first_occurrence(data, element):
    for index, value in enumerate(data):
        if value == element:
            return index
    return -1
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 5]
    element1 = 5
    result1 = find_first_occurrence(list1, element1)
    print(f"List: {list1}, Element: {element1}, Index: {result1}")
    list2 = [10, 20, 30, 40]
    element2 = 5
    result2 = find_first_occurrence(list2, element2)
    print(f"List: {list2}, Element: {element2}, Index: {result2}")
    list3 = ['a', 'b', 'c', 'a']
    element3 = 'a'
    result3 = find_first_occurrence(list3, element3)
    print(f"List: {list3}, Element: {element3}, Index: {result3}")
    list4 = [100, 200, 300]
    element4 = 400
    result4 = find_first_occurrence(list4, element4)
    print(f"List: {list4}, Element: {element4}, Index: {result4}")