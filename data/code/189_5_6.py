def remove_last_element(data_list):
    if data_list:
        data_list.pop(-1)
    return data_list

if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    result1 = remove_last_element(list1)
    print(f"List after removing last element: {result1}")
    
    empty_list = []
    result2 = remove_last_element(empty_list)
    print(f"Empty list after attempting to remove last element: {result2}")