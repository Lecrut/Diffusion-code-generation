import itertools

def interleave_lists(list1, list2):
    return [item for sublist in itertools.zip_longest(list1, list2, fillvalue=None) for item in sublist if item is not None]

if __name__ == '__main__':
    sample_list1 = [1, 3, 5]
    sample_list2 = [2, 4, 6]
    interleaved_result = interleave_lists(sample_list1, sample_list2)
    print(interleaved_result)