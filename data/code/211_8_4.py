from itertools import chain, islice

def compare_tuples(list1, list2):
    return set(chain.from_iterable(islice(lst, 1, None) for lst in (list1, list2))) == set()

if __name__ == '__main__':
    sample_list1 = [(1, 2), (3, 4), (5, 6)]
    sample_list2 = [(6, 5), (4, 3), (2, 1)]
    print(compare_tuples(sample_list1, sample_list2))