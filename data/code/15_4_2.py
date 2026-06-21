def get_penultimate_element(data):
    if len(data) < 2:
        return None
    return data[-2]

if __name__ == '__main__':
    sample_list_full = [10, 20, 30, 40, 50]
    sample_list_single = [42]
    sample_list_empty = []
    
    result_full = get_penultimate_element(sample_list_full)
    result_single = get_penultimate_element(sample_list_single)
    result_empty = get_penultimate_element(sample_list_empty)
    
    print(result_full)
    print(result_single)
    print(result_empty)