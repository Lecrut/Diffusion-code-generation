from itertools import chain, starmap

def compare_tuples(list1, list2):
    return set(map(tuple, list1)) == set(map(tuple, list2))

if __name__ == '__main__':
    sample_list1 = [(1, 2), (3, 4)]
    sample_list2 = [(4, 3), (2, 1)]
    print(compare_tuples(sample_list1, sample_list2))