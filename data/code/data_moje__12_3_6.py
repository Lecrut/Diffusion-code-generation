def get_middle_element(lst):
    if not lst:
        raise ValueError("List is empty")
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    print(get_middle_element(sample_list1))
    sample_list2 = [10, 20, 30]
    print(get_middle_element(sample_list2))
    sample_list3 = [7]
    print(get_middle_element(sample_list3))