def find_middle_element(lst):
    mid_index = len(lst) // 2
    return lst[mid_index] if len(lst) % 2 != 0 else (lst[mid_index - 1], lst[mid_index])

if __name__ == '__main__':
    sample_list = [4, 7, 2, 5, 8]
    print(find_middle_element(sample_list))