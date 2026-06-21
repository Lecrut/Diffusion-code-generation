def get_middle_element(lst):
    if not lst:
        return None
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60, 70]
    middle = get_middle_element(sample_list)
    print(middle)
    even_list = [1, 2, 3, 4]
    middle_even = get_middle_element(even_list)
    print(middle_even)