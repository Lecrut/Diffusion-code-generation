def remove_item(data_list, value):
    try:
        index = data_list.index(value)
        data_list.pop(index)
    except ValueError:
        pass
    return data_list
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 2, 5]
    value1 = 2
    result1 = remove_item(list1, value1)
    print(f"Original list: [1, 2, 3, 4, 2, 5], Value to remove: {value1}")
    print(f"Result list: {result1}")
    list2 = [10, 20, 30, 40]
    value2 = 99
    result2 = remove_item(list2, value2)
    print(f"\nOriginal list: [10, 20, 30, 40], Value to remove: {value2}")
    print(f"Result list: {result2}")
    list3 = [5, 5, 5]
    value3 = 5
    result3 = remove_item(list3, value3)
    print(f"\nOriginal list: [5, 5, 5], Value to remove: {value3}")
    print(f"Result list: {result3}")
    list4 = [1, 2, 3]
    value4 = 4
    result4 = remove_item(list4, value4)
    print(f"\nOriginal list: [1, 2, 3], Value to remove: {value4}")
    print(f"Result list: {result4}")