def find_middle_element(lst):
    length = len(lst)
    middle_index = length // 2
    return lst[middle_index]
if __name__ == '__main__':
    sample_list_odd = [1, 2, 3, 4, 5]
    sample_list_even = [1, 2, 3, 4]
    print(find_middle_element(sample_list_odd))
    print(find_middle_element(sample_list_even))