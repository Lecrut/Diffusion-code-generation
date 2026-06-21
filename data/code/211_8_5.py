import itertools

def compare_tuples(list1, list2):
    set1 = set(map(tuple, list1))
    set2 = set(map(tuple, list2))
    return set1 == set2

if __name__ == '__main__':
    sample_list1 = [(5, 6), (7, 8)]
    sample_list2 = [(8, 7), (6, 5)]
    print(compare_tuples(sample_list1, sample_list2))