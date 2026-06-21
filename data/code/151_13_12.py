import itertools

def combine_lists(list1, list2):
    combined = list(itertools.chain(list1, list2))
    return combined

if __name__ == '__main__':
    sample_list1 = [4, 9, 1, 6]
    sample_list2 = ['x', 'y', 'z']
    combined_result = combine_lists(sample_list1, sample_list2)
    print(combined_result)