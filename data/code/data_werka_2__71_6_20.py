def find_median(lst):
    if not lst:
        raise ValueError("List must not be empty")
    
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    
    if n % 2 == 1:
        return sorted_lst[n // 2]
    else:
        lower_middle_index = (n // 2) - 1
        return sorted_lst[lower_middle_index]

if __name__ == '__main__':
    sample_list_odd = [7, 1, 3, 5, 9]
    sample_list_even = [4, 2, 8, 6]
    
    result_odd = find_median(sample_list_odd)
    result_even = find_median(sample_list_even)
    
    print(result_odd)
    print(result_even)