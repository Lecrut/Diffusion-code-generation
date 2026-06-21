import itertools

def compare_tuples(list1, list2):
    return set(tuple(sorted(tup)) for tup in list1) == set(tuple(sorted(tup)) for tup in list2)

if __name__ == '__main__':
    sample_list1 = [(1, 2), (3, 4)]
    sample_list2 = [(4, 3), (2, 1)]
    print(compare_tuples(sample_list1, sample_list2))