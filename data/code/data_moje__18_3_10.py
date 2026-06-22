def get_central_element(lst):
    if not lst:
        return None
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_central_element(sample_list)
    print(result)
    
    sample_list_odd = [10, 20, 30, 40]
    result_odd = get_central_element(sample_list_odd)
    print(result_odd)