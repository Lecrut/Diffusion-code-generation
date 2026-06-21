import itertools

def are_tuples_equal(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    
    if len(list1) != len(list2):
        return False
    
    sorted_list1 = sorted([sorted(tup) for tup in list1])
    sorted_list2 = sorted([sorted(tup) for tup in list2])
    
    return sorted_list1 == sorted_list2

if __name__ == '__main__':
    sample_list1 = [(1, 2), (3, 4)]
    sample_list2 = [(4, 3), (2, 1)]
    print(are_tuples_equal(sample_list1, sample_list2))