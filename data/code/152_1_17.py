def find_common_elements(list1, list2):
    if not all(isinstance(item, list) for item in (list1, list2)):
        raise ValueError("Both inputs must be lists.")
    
    common = []
    seen_in_list2 = set()
    for item in list1:
        if item in list2 and item not in seen_in_list2:
            common.append(item)
            seen_in_list2.add(item)
    return common

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5, 6]
    sample_list2 = [4, 5, 6, 7, 8, 9]
    print(find_common_elements(sample_list1, sample_list2))