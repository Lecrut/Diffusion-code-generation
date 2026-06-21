def intersect_sorted_lists(list1, list2):
    return sorted(set(list1) & set(list2))

if __name__ == '__main__':
    sample_list1 = [3, 5, 2, 8, 4]
    sample_list2 = [1, 2, 3, 7, 5]
    print(intersect_sorted_lists(sample_list1, sample_list2))