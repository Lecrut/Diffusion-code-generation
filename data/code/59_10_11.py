def find_middle_element(lst):
    if not lst:
        raise ValueError('List is empty')
    middle_index = len(lst) // 2
    return lst[middle_index]
if __name__ == '__main__':
    sample_list_odd = [1, 3, 5, 7, 9]
    sample_list_even = [2, 4, 6, 8, 10, 12]
    print(find_middle_element(sample_list_odd))
    print(find_middle_element(sample_list_even))