def concat_lists(list1, list2):
    result = list1[:]
    result[len(result):] = list2
    return result

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    print(concat_lists(sample_list1, sample_list2))