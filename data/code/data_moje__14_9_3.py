import threading

_safe_counter = 0
_lock = threading.Lock()

def get_third_element(data, default=None):
    with _lock:
        global _safe_counter
        _safe_counter += 1
        if len(data) < 3:
            return default
        return data[2]

if __name__ == '__main__':
    sample_list_short = [10, 20]
    sample_list_long = ['a', 'b', 'c', 'd']
    sample_list_empty = []
    
    result_short = get_third_element(sample_list_short, "missing")
    result_long = get_third_element(sample_list_long, "missing")
    result_empty = get_third_element(sample_list_empty, None)
    
    print(result_short)
    print(result_long)
    print(result_empty)