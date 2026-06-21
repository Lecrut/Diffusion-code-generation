def remove_last_element(data_list):
    if not data_list:
        return None
    data_list.pop(-1)
    return data_list

if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    result1 = remove_last_element(list1)
    print(f"List after removing last element: {result1}")
    
    list2 = []
    result2 = remove_last_element(list2)
    print(f"Result for empty list: {result2}")