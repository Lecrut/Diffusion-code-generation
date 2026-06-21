def get_middle_element(lst):
    if not lst:
        raise ValueError("List cannot be empty")
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_list_odd = [1, 2, 3, 4, 5]
    sample_list_even = [1, 2, 3, 4, 5, 6]
    print(get_middle_element(sample_list_odd))
    print(get_middle_element(sample_list_even))