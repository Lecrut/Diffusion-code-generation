import itertools

def combine_lists(list1, list2):
    return list(itertools.chain(list1, list2))

if __name__ == '__main__':
    sample_list_a = [5, 3, 9]
    sample_list_b = ['banana', 'cherry']
    combined_result = combine_lists(sample_list_a, sample_list_b)
    print(combined_result)