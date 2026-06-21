def are_lists_lexicographically_smaller(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    min_len = min(len1, len2)
    for i in range(min_len):
        if list1[i] < list2[i]:
            return True
        elif list1[i] > list2[i]:
            return False
    return len1 < len2
if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [1, 2, 4]
    print(are_lists_lexicographically_smaller(sample_list1, sample_list2))
    sample_list3 = [1, 2, 3]
    sample_list4 = [1, 2, 3]
    print(are_lists_lexicographically_smaller(sample_list3, sample_list4))
    sample_list5 = [1, 2, 3]
    sample_list6 = [1, 2]
    print(are_lists_lexicographically_smaller(sample_list5, sample_list6))