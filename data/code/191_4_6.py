def merge_tuple_lists(list1, list2):
    return list1 + list2

if __name__ == '__main__':
    sample_list1 = [(10, 20), (30, 40)]
    sample_list2 = [(50, 60), (70, 80)]
    result = merge_tuple_lists(sample_list1, sample_list2)
    print(result)