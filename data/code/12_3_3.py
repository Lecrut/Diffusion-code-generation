def get_middle_element(lst):
    length = len(lst)
    if length == 0:
        return None
    mid_index = length // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_list_odd = [1, 2, 3, 4, 5]
    sample_list_even = [10, 20, 30, 40]
    sample_list_single = [42]
    sample_list_empty = []
    
    print(get_middle_element(sample_list_odd))
    print(get_middle_element(sample_list_even))
    print(get_middle_element(sample_list_single))
    print(get_middle_element(sample_list_empty))