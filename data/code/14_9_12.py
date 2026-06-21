import threading

_lock = threading.Lock()

def safe_extract_third(data, default=None):
    with _lock:
        if isinstance(data, list) and len(data) >= 3:
            return data[2]
        return default

if __name__ == '__main__':
    list_short = [1, 2]
    list_long = [10, 20, 30, 40]
    result_short = safe_extract_third(list_short, 'default')
    result_long = safe_extract_third(list_long, 'default')
    print(result_short)
    print(result_long)