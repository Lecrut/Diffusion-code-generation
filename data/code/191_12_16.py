import itertools

def combine_lists(list1, list2):
    return list(itertools.chain(list1, list2))

if __name__ == '__main__':
    sample_list1 = [7, 8, 9]
    sample_list2 = ['m', 'n', 'o']
    combined_result = combine_lists(sample_list1, sample_list2)
    print(combined_result)