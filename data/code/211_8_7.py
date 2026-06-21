import itertools

def compare_tuples(list1, list2):
    return set(list1) == set(list2)

if __name__ == '__main__':
    sample_list1 = [(1, 2), (3, 4)]
    sample_list2 = [(3, 4), (1, 2)]
    print(compare_tuples(sample_list1, sample_list2))