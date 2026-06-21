import itertools

def interleave_lists(list1, list2):
    return [item for sublist in itertools.chain.from_iterable(zip(list1, list2)) for item in sublist]

if __name__ == '__main__':
    sample_list1 = ['a', 'c', 'e']
    sample_list2 = ['b', 'd', 'f']
    interleaved_result = interleave_lists(sample_list1, sample_list2)
    print(interleaved_result)