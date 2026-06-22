def get_middle_element(lst):
    if not lst:
        return None
    return lst[len(lst) // 2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_middle_element(sample_list))

    sample_list_even = [1, 2, 3, 4]
    print(get_middle_element(sample_list_even))

    empty_list = []
    print(get_middle_element(empty_list))

    single_element = [42]
    print(get_middle_element(single_element))