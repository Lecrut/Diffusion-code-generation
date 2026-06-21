def get_middle_item(lst):
    if not lst:
        return None
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_middle_item(sample_list))

    sample_list_even = [1, 2, 3, 4]
    print(get_middle_item(sample_list_even))

    single_item = [42]
    print(get_middle_item(single_item))

    empty_list = []
    print(get_middle_item(empty_list))