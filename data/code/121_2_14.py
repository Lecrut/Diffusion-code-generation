def compare_lists(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    if len1 > len2:
        return list1
    elif len2 > len1:
        return list2
    else:
        return None

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [6, 7, 8, 9]
    longer_list = compare_lists(sample_list1, sample_list2)
    print(longer_list)