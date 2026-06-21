def intersect_sorted_lists(list1, list2):
    return sorted(set(list1) & set(list2))

if __name__ == '__main__':
    sample_list1 = [3, 5, 6, 8, 9]
    sample_list2 = [2, 3, 4, 5, 7]
    print(intersect_sorted_lists(sample_list1, sample_list2))