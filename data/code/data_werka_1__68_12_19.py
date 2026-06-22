def find_difference(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    
    set1 = set(list1)
    set2 = set(list2)
    
    return list(set1 - set2)

if __name__ == '__main__':
    sample_list1 = [15, 20, 25, 30, 35]
    sample_list2 = [25, 30, 35, 40, 45]
    result = find_difference(sample_list1, sample_list2)
    print(result)