def get_middle_element(lst):
    if not lst:
        return None
    index = len(lst) // 2
    return lst[index]

if __name__ == '__main__':
    sample_list_odd = [1, 2, 3, 4, 5]
    sample_list_even = [1, 2, 3, 4]
    sample_list_single = [42]
    
    print(get_middle_element(sample_list_odd))
    print(get_middle_element(sample_list_even))
    print(get_middle_element(sample_list_single))
    print(get_middle_element([]))