def find_median(lst):
    if not lst:
        raise ValueError("List must not be empty")
    
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    
    if n % 2 == 1:
        return sorted_lst[n // 2]
    else:
        return sorted_lst[(n // 2) - 1]

if __name__ == '__main__':
    sample_list = [7, 1, 3, 4, 6, 5, 2]
    result = find_median(sample_list)
    print(result)
    
    sample_list_even = [7, 1, 3, 4, 6, 5]
    result_even = find_median(sample_list_even)
    print(result_even)