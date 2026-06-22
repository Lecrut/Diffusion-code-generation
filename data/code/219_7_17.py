def compare_lists(list1, list2):
    return [max(a, b) for a, b in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [3, 5, 7]
    sample_list2 = [2, 6, 4]
    print(compare_lists(sample_list1, sample_list2))