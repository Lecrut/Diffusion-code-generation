import threading

_lock = threading.Lock()

def get_third_element(lst, default=None):
    with _lock:
        if len(lst) >= 3:
            return lst[2]
        return default

if __name__ == '__main__':
    result = get_third_element([1, 2, 3, 4])
    print(result)
    result_short = get_third_element([1, 2])
    print(result_short)
    result_empty = get_third_element([], "default")
    print(result_empty)