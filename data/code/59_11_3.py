def find_middle_element(lst):
    index = len(lst) // 2
    return lst[index]
if __name__ == '__main__':
    sample_list_odd = [3, 1, 4, 1, 5]
    sample_list_even = [3, 1, 4, 1]
    print(find_middle_element(sample_list_odd))
    print(find_middle_element(sample_list_even))