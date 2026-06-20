def list_operations(list1, list2, operation):
    if operation == 'intersection':
        return [value for value in list1 if value in list2]
    elif operation == 'union':
        return list(set(list1 + list2))
    elif operation == 'difference':
        return [value for value in list1 if value not in list2]
    else:
        raise ValueError("Invalid operation")

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    print(list_operations(list1, list2, 'intersection'))
    print(list_operations(list1, list2, 'union'))
    print(list_operations(list1, list2, 'difference'))