def safe_remove(data_list, element):
    try:
        data_list.remove(element)
        return "success"
    except ValueError:
        return "not_found"
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    element1 = 3
    result1 = safe_remove(list1, element1)
    print(f"List: {list1}, Element to remove: {element1}, Result: {result1}")
    list2 = [10, 20, 30]
    element2 = 99
    result2 = safe_remove(list2, element2)
    print(f"List: {list2}, Element to remove: {element2}, Result: {result2}")
    list3 = ['a', 'b', 'c']
    element3 = 'd'
    result3 = safe_remove(list3, element3)
    print(f"List: {list3}, Element to remove: {element3}, Result: {result3}")
    list4 = [50]
    element4 = 50
    result4 = safe_remove(list4, element4)
    print(f"List: {list4}, Element to remove: {element4}, Result: {result4}")