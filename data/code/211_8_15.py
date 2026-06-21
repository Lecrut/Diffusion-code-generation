from itertools import islice

def compare_tuples(list1, list2):
    return sorted(list1) == sorted(list2)

if __name__ == '__main__':
    sample_list1 = [(3, 2), (1, 4)]
    sample_list2 = [(4, 1), (2, 3)]
    print(compare_tuples(sample_list1, sample_list2))