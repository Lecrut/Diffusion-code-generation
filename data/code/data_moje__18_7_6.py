def get_middle_item(lst):
    if not lst:
        return None
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_middle_item(sample_list))
    
    sample_list_even = [10, 20, 30, 40]
    print(get_middle_item(sample_list_even))
    
    sample_list_single = [42]
    print(get_middle_item(sample_list_single))
    
    sample_list_empty = []
    print(get_middle_item(sample_list_empty))