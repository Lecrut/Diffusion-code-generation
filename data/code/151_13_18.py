import itertools

def combine_and_chain(list1, list2):
    combined = itertools.chain(list1, list2)
    return list(combined)

if __name__ == '__main__':
    sample_list1 = [1, 5, 2, 8, 5]
    sample_list2 = [8, 3, 1, 9, 2]
    result = combine_and_chain(sample_list1, sample_list2)
    print(result)