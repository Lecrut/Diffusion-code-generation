def max_pairs(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both arguments must be lists.")
    
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")
    
    return [max(a, b) for a, b in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [4, 6, 8]
    sample_list2 = [3, 9, 7]
    print(max_pairs(sample_list1, sample_list2))