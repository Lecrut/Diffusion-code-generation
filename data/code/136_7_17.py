def set_operations(list1, list2, operation):
    if operation == 'intersection':
        return set(list1).intersection(set(list2))
    elif operation == 'union':
        return set(list1).union(set(list2))
    elif operation == 'difference':
        return set(list1).difference(set(list2))
    else:
        raise ValueError('Unsupported operation')
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    print(set_operations(list1, list2, 'intersection'))
    print(set_operations(list1, list2, 'union'))
    print(set_operations(list1, list2, 'difference'))