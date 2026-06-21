def remove_last_element(data_list):
    if data_list:
        data_list.pop(-1)
    return data_list

if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    result1 = remove_last_element(list1)
    print(f"List: {list1}, Result: {result1}")
    
    list2 = []
    result2 = remove_last_element(list2)
    print(f"List: {list2}, Result: {result2}")