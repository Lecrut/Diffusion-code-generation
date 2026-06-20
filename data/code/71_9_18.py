def find_middle_element(lst):
    n = len(lst)
    middle_index = (n - 1) // 2
    return lst[middle_index]
if __name__ == '__main__':
    sample_list_odd = [9, 8, 7, 6, 5]
    print(find_middle_element(sample_list_odd))
    sample_list_even = [10, 20, 30, 40]
    print(find_middle_element(sample_list_even))