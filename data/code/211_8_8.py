import itertools

def tuples_to_sets(list_of_tuples):
    return {frozenset(t) for t in list_of_tuples}

def compare_lists(list1, list2):
    set1 = tuples_to_sets(list1)
    set2 = tuples_to_sets(list2)
    return set1 == set2

if __name__ == '__main__':
    sample_list1 = [(1, 2), (3, 4)]
    sample_list2 = [(4, 3), (2, 1)]
    print(compare_lists(sample_list1, sample_list2))