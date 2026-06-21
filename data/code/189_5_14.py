def safe_remove(data_list):
    if not data_list:
        return "List is empty"
    removed = data_list.pop(-1)
    return f"Removed: {removed}, New list: {data_list}"

if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    result1 = safe_remove(list1)
    print(result1)
    
    list2 = [10, 20, 30]
    result2 = safe_remove(list2)
    print(result2)
    
    list3 = []
    result3 = safe_remove(list3)
    print(result3)