import itertools

def combine_and_sort(list1, list2):
    combined = list(itertools.chain(list1, list2))
    sorted_combined = sorted(combined)
    return sorted_combined

if __name__ == '__main__':
    sample_list1 = [5, 3, 9]
    sample_list2 = ['b', 'a', 'c']
    result = combine_and_sort(sample_list1, sample_list2)
    print(result)