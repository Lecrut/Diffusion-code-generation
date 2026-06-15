def safe_remove(data_list, element):
    try:
        data_list.remove(element)
        return "Success"
    except ValueError:
        return "Element not found"
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    element1 = 3
    result1 = safe_remove(list1, element1)
    print(f"List before: {list1}")
    print(f"Attempt to remove {element1}: {result1}")
    print(f"List after: {list1}\n")
    list2 = [10, 20, 30]
    element2 = 99
    result2 = safe_remove(list2, element2)
    print(f"List before: {list2}")
    print(f"Attempt to remove {element2}: {result2}")
    print(f"List after: {list2}\n")
    list3 = ['a', 'b', 'c']
    element3 = 'd'
    result3 = safe_remove(list3, element3)
    print(f"List before: {list3}")
    print(f"Attempt to remove {element3}: {result3}")
    print(f"List after: {list3}\n")