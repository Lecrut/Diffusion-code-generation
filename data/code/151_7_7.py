import itertools

def interleave_lists(list1, list2):
    interleaved = []
    for item1, item2 in itertools.zip_longest(list1, list2):
        if item1 is not None:
            interleaved.append(item1)
        if item2 is not None:
            interleaved.append(item2)
    return interleaved

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = [40, 50]
    result = interleave_lists(sample_list1, sample_list2)
    print(result)