import threading

_safe_lock = threading.Lock()

def get_third_element(data, default=None):
    with _safe_lock:
        if len(data) >= 3:
            return data[2]
        return default

if __name__ == '__main__':
    sample_list_short = [1, 2]
    sample_list_long = [10, 20, 30, 40]
    result_short = get_third_element(sample_list_short, default="N/A")
    result_long = get_third_element(sample_list_long)
    print(result_short)
    print(result_long)