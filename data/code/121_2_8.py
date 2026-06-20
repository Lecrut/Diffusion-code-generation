def longer_list(list1, list2):
    return list1 if len(list1) > len(list2) else list2

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6, 7]
    print(longer_list(sample_list1, sample_list2))