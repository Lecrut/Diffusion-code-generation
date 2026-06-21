def get_middle_element(lst):
    if not lst:
        raise ValueError("List is empty")
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_middle_element(sample_list))
    sample_list_even = [1, 2, 3, 4]
    print(get_middle_element(sample_list_even))
    single_element = [42]
    print(get_middle_element(single_element))