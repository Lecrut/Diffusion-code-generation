def find_common_elements(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    
    def is_unique_in_list(element, target_list):
        return element in target_list
    
    common_elements = []
    for item in list1:
        if is_unique_in_list(item, list2) and item not in common_elements:
            common_elements.append(item)
    
    return common_elements

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5, 5]
    sample_list2 = [4, 5, 6, 7, 8, 4]
    result = find_common_elements(sample_list1, sample_list2)
    print(result)