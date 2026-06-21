import itertools

def compare_tuples(list1, list2):
    if not all(isinstance(item, tuple) for item in list1 + list2):
        raise ValueError("Both lists must contain only tuples.")
    
    return set(tuple(sorted(tup)) for tup in list1) == set(tuple(sorted(tup)) for tup in list2)

if __name__ == '__main__':
    sample_list1 = [(1, 2), (3, 4)]
    sample_list2 = [(4, 3), (2, 1)]
    print(compare_tuples(sample_list1, sample_list2))