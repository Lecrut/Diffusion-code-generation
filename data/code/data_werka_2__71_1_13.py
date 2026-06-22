def find_middle(lst):
    if not lst:
        raise ValueError("List must not be empty")
    n = len(lst)
    mid_index = (n - 1) // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_list_odd = [10, 20, 30, 40, 50]
    sample_list_even = [10, 20, 30, 40]
    
    result_odd = find_middle(sample_list_odd)
    result_even = find_middle(sample_list_even)
    
    print(result_odd)
    print(result_even)