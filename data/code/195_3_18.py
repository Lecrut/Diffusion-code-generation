def count_common_elements(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    
    common_count = 0
    for element in set(list1):
        if element in list2:
            common_count += min(list1.count(element), list2.count(element))
    
    return common_count

if __name__ == '__main__':
    sample_list_a = ["apple", "banana", "cherry", "date", "elderberry"]
    sample_list_b = ["apple", "orange", "cherry", "grape", "elderberry"]
    result = count_common_elements(sample_list_a, sample_list_b)
    print(f"Count of common elements: {result}")