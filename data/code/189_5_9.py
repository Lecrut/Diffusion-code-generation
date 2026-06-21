def safe_remove(data_list):
    if not data_list:
        return "List is empty"
    removed_element = data_list.pop(-1)
    return f"Removed element: {removed_element}"

if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    result1 = safe_remove(list1)
    print(f"List after removal: {list1}, Result: {result1}")
    
    list2 = []
    result2 = safe_remove(list2)
    print(f"List after removal: {list2}, Result: {result2}")