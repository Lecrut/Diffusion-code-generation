def combine_booleans(list1, list2):
    return [x or y for x, y in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [True, False, True]
    sample_list2 = [False, True, False]
    result = combine_booleans(sample_list1, sample_list2)
    print(result)