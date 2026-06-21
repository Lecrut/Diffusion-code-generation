import itertools

def interleave_lists(list1, list2):
    interleaved = [item for sublist in itertools.zip_longest(list1, list2) for item in sublist if item is not None]
    return interleaved

if __name__ == '__main__':
    sample_list1 = [7, 5, 3, 1]
    sample_list2 = [8, 6, 4, 2]
    result = interleave_lists(sample_list1, sample_list2)
    print(result)