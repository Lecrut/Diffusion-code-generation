from itertools import chain, islice

def compare_tuples(list1, list2):
    return set(map(tuple, list1)) == set(map(tuple, list2))

if __name__ == '__main__':
    sample_list1 = [(1, 2), (3, 4), (5, 6)]
    sample_list2 = [(6, 5), (4, 3), (2, 1)]
    
    result = compare_tuples(sample_list1, sample_list2)
    print(result)