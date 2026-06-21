import threading

safe_index_lock = threading.Lock()

def get_third_element_safe(data_list, default_value=None):
    with safe_index_lock:
        if len(data_list) >= 3:
            return data_list[2]
        return default_value

if __name__ == '__main__':
    sample_list_short = [1, 2]
    sample_list_long = ['a', 'b', 'c', 'd']
    sample_default = "Not Available"
    
    result_short = get_third_element_safe(sample_list_short, sample_default)
    result_long = get_third_element_safe(sample_list_long, sample_default)
    
    print(result_short)
    print(result_long)