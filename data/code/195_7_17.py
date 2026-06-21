def are_permutations(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    
    return sorted(list1) == sorted(list2)

if __name__ == '__main__':
    sample_list1 = [3, 5, 2, 8]
    sample_list2 = [2, 5, 3, 8]
    result = are_permutations(sample_list1, sample_list2)
    print(result)