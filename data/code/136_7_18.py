def list_operation(list1, list2, operation):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists")
    
    if operation == 'intersection':
        result = [item for item in list1 if item in list2]
    elif operation == 'union':
        result = list(set(list1 + list2))
    elif operation == 'difference':
        result = [item for item in list1 if item not in list2]
    else:
        raise ValueError("Invalid operation. Choose from 'intersection', 'union', or 'difference'")
    
    return result

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    operation = 'intersection'
    print(list_operation(sample_list1, sample_list2, operation))