import itertools

def interleave_lists(list1, list2):
    return [item for sublist in itertools.chain.from_iterable(zip(list1, list2)) for item in sublist]

if __name__ == '__main__':
    sample_list1 = [1, 3, 5]
    sample_list2 = [2, 4, 6]
    print(interleave_lists(sample_list1, sample_list2))