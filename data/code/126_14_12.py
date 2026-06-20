def lists_equal(lst1: list, lst2: list) -> bool:
    return lst1 == lst2

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [1, 2, 3]
    sample_list3 = [3, 2, 1]

    print(f"lists_equal(sample_list1, sample_list2): {lists_equal(sample_list1, sample_list2)}")
    print(f"lists_equal(sample_list1, sample_list3): {lists_equal(sample_list1, sample_list3)}")