def find_middle_element(lst):
    if not lst:
        raise ValueError("List must not be empty")
    n = len(lst)
    index = (n - 1) // 2
    return lst[index]

if __name__ == '__main__':
    sample_list_odd = [10, 20, 30, 40, 50]
    sample_list_even = [10, 20, 30, 40]
    
    result_odd = find_middle_element(sample_list_odd)
    result_even = find_middle_element(sample_list_even)
    
    print(result_odd)
    print(result_even)