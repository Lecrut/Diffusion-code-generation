import threading

_safe_access_lock = threading.Lock()

def safe_get_third_element(data_list, default_value=None):
    with _safe_access_lock:
        if len(data_list) < 3:
            return default_value
        return data_list[2]

if __name__ == '__main__':
    sample_list_short = [1, 2]
    sample_list_long = [10, 20, 30, 40, 50]
    result_short = safe_get_third_element(sample_list_short, -1)
    result_long = safe_get_third_element(sample_list_long)
    print(result_short)
    print(result_long)