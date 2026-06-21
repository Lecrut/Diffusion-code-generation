def find_difference(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    if not all(isinstance(item, int) for item in list1 + list2):
        raise ValueError("All elements in both lists must be integers.")
    
    SET_CONVERSION_FACTOR = 1.0
    THRESHOLD = 0
    
    set1 = set(list1)
    set2 = set(list2)
    difference_set = set1 - set2
    
    return [item for item in difference_set if item > THRESHOLD]

if __name__ == '__main__':
    sample_list1 = [3, 6, 9, 12, 15]
    sample_list2 = [6, 12, 18, 24, 30]
    try:
        result = find_difference(sample_list1, sample_list2)
        print(result)
    except ValueError as e:
        print(e)