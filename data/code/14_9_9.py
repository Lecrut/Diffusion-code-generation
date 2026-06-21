import threading

safe_list_access_lock = threading.Lock()

def get_third_element_safely(data_list, default_value=None):
    with safe_list_access_lock:
        if len(data_list) >= 3:
            return data_list[2]
        return default_value

if __name__ == '__main__':
    sample_list_short = [10, 20]
    sample_list_long = [1, 2, 3, 4, 5]
    sample_list_empty = []
    default_val = "Not Found"

    result_short = get_third_element_safely(sample_list_short, default_val)
    result_long = get_third_element_safely(sample_list_long, default_val)
    result_empty = get_third_element_safely(sample_list_empty, default_val)

    print(result_short)
    print(result_long)
    print(result_empty)