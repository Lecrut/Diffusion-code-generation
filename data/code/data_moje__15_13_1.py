def penultimate(lst):
    if lst is None:
        return None
    n = len(lst)
    if n < 2:
        return None
    return lst[n - 2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = penultimate(sample_list)
    print(result)
    
    empty_list = []
    result_empty = penultimate(empty_list)
    print(result_empty)
    
    single_list = [100]
    result_single = penultimate(single_list)
    print(result_single)