def compare_lists(list1, list2, operation):
    if operation == 'intersection':
        return [item for item in list1 if item in list2]
    elif operation == 'union':
        return list(set(list1 + list2))
    elif operation == 'difference':
        return [item for item in list1 if item not in list2]
    else:
        raise ValueError("Invalid operation. Supported operations: 'intersection', 'union', 'difference'")
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    operation = 'intersection'
    result = compare_lists(list1, list2, operation)
    print(result)
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    operation = 'union'
    result = compare_lists(list1, list2, operation)
    print(result)
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    operation = 'difference'
    result = compare_lists(list1, list2, operation)
    print(result)