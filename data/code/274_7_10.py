def find_common_elements(list1, list2):
    if not all(isinstance(lst, list) and isinstance(item, (int, float)) for lst in [list1, list2] for item in lst):
        raise ValueError("Both inputs must be lists containing only integers or floats")
    
    common = set(list1).intersection(set(list2))
    return common

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    try:
        print(find_common_elements(sample_list1, sample_list2))
    except ValueError as e:
        print(e)