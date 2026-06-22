def find_difference(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    if not all(isinstance(item, int) for item in list1 + list2):
        raise ValueError("All elements in both lists must be integers.")
    
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 - set2)

if __name__ == '__main__':
    sample_list1 = [5, 7, 9, 10, 15]
    sample_list2 = [10, 15, 20, 25, 30]
    try:
        result = find_difference(sample_list1, sample_list2)
        print(result)
    except ValueError as e:
        print(e)