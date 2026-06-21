import itertools

def concatenate_lists(list1, list2):
    return list(itertools.chain(list1, list2))

if __name__ == '__main__':
    sample_list_a = [10, 20, 30]
    sample_list_b = ['a', 'b', 'c']
    result = concatenate_lists(sample_list_a, sample_list_b)
    print(result)