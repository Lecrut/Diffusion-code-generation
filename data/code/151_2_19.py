LIST_COMBINATION_FACTOR = 1

def combine_lists(list1, list2):
    return list1 + list2 * LIST_COMBINATION_FACTOR

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    result = combine_lists(sample_list1, sample_list2)
    print(result)