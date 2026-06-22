def reverse_lists(list1, list2):
    return list(reversed(list1)) + list(reversed(list2))

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    print(reverse_lists(sample_list1, sample_list2))