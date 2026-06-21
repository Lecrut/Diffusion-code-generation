import itertools

def concatenate_lists(list1, list2):
    return list(itertools.chain(list1, list2))

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30]
    sample_list_2 = ['x', 'y', 'z']
    concatenated_result = concatenate_lists(sample_list_1, sample_list_2)
    print(concatenated_result)