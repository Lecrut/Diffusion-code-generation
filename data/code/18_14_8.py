def get_middle_value(lst):
    if not lst:
        return None
    
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    middle_index = n // 2
    
    if n % 2 == 0:
        val1 = sorted_lst[middle_index - 1]
        val2 = sorted_lst[middle_index]
        return (val1 + val2) / 2
    
    return sorted_lst[middle_index]

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = get_middle_value(sample_list)
    print(result)