def safe_remove_last(data_list):
    if not data_list:
        return "List is empty"
    
    data_list.pop(-1)
    return "Success"

if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    result1 = safe_remove_last(list1)
    print(f"List: {list1}, Result: {result1}")
    
    list2 = [10, 20, 30]
    result2 = safe_remove_last(list2)
    print(f"List: {list2}, Result: {result2}")
    
    list3 = []
    result3 = safe_remove_last(list3)
    print(f"List: {list3}, Result: {result3}")