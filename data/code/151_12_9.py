def join_lists(list1, list2):
    return [*list1, *list2]

if __name__ == '__main__':
    sample_list1 = [13, 14, 15]
    sample_list2 = [16, 17, 18]
    result = join_lists(sample_list1, sample_list2)
    print(result)