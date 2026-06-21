import itertools

def combine_lists(list1, list2):
    combined_generator = itertools.chain(list1, list2)
    return list(combined_generator)

if __name__ == '__main__':
    sample_list1 = [4, 7, 1]
    sample_list2 = ['d', 'a', 'e']
    result = combine_lists(sample_list1, sample_list2)
    print(result)