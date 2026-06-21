import itertools

def are_tuples_equal(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both arguments must be lists.")
    
    if len(list1) != len(list2):
        return False
    
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    
    for tuple1, tuple2 in itertools.zip_longest(sorted_list1, sorted_list2):
        if tuple1 != tuple2:
            return False
    
    return True

if __name__ == '__main__':
    sample_list1 = [(1, 2), (3, 4)]
    sample_list2 = [(4, 3), (2, 1)]
    print(are_tuples_equal(sample_list1, sample_list2))