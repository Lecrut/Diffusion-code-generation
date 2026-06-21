import itertools

def compare_tuples(list1, list2):
    set1 = set(tuple(sorted(t)) for t in list1)
    set2 = set(tuple(sorted(t)) for t in list2)
    return set1 == set2

if __name__ == '__main__':
    sample_list1 = [(1, 2), (3, 4)]
    sample_list2 = [(4, 3), (2, 1)]
    print(compare_tuples(sample_list1, sample_list2))