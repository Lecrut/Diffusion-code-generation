def find_middle(lst):
    if not lst:
        raise ValueError("List must not be empty")
    length = len(lst)
    mid_index = (length - 1) // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_list_odd = [1, 2, 3, 4, 5]
    sample_list_even = [1, 2, 3, 4]
    
    result_odd = find_middle(sample_list_odd)
    result_even = find_middle(sample_list_even)
    
    print(result_odd)
    print(result_even)