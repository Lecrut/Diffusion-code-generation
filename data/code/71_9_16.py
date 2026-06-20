def find_middle_element(lst):
    return lst[(len(lst) - 1) // 2]

if __name__ == '__main__':
    sample_list = [3, 5, 2, 8, 1, 4]
    print(find_middle_element(sample_list))
    sample_list_even = [1, 2, 3, 4]
    print(find_middle_element(sample_list_even))
    sample_list_odd = [100, 200, 300]
    print(find_middle_element(sample_list_odd))