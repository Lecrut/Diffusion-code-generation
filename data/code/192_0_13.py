def find_common_elements(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    
    common_elements = set()
    for item in list1:
        if item in list2 and item not in common_elements:
            common_elements.add(item)
    
    return sorted(common_elements)

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5, 5]
    list_b = [4, 5, 6, 7, 8, 4]
    result = find_common_elements(list_a, list_b)
    print(result)