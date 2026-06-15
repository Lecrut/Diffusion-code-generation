def find_first_occurrence(data, element):
    for index, value in enumerate(data):
        if value == element:
            return index
    return -1
if __name__ == '__main__':
    list1 = [10, 20, 30, 20, 40]
    element1 = 20
    result1 = find_first_occurrence(list1, element1)
    print(f"List: {list1}, Element: {element1}, Index: {result1}")
    list2 = [5, 15, 25, 35]
    element2 = 10
    result2 = find_first_occurrence(list2, element2)
    print(f"List: {list2}, Element: {element2}, Index: {result2}")
    list3 = [1, 2, 3]
    element3 = 4
    result3 = find_first_occurrence(list3, element3)
    print(f"List: {list3}, Element: {element3}, Index: {result3}")
    list4 = ['a', 'b', 'c', 'a']
    element4 = 'a'
    result4 = find_first_occurrence(list4, element4)
    print(f"List: {list4}, Element: {element4}, Index: {result4}")