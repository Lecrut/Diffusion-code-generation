def get_middle_item(lst):
    if not lst:
        return None
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [10, 20, 30, 40, 50, 60]
    sample_list3 = [7]
    sample_list4 = []

    print(get_middle_item(sample_list1))
    print(get_middle_item(sample_list2))
    print(get_middle_item(sample_list3))
    print(get_middle_item(sample_list4))