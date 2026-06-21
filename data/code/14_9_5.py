import threading

_lock = threading.Lock()

def get_third_element(lst, default=None):
    with _lock:
        if len(lst) >= 3:
            return lst[2]
        return default

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    short_list = [1, 2]
    empty_list = []

    result1 = get_third_element(sample_list)
    print(result1)

    result2 = get_third_element(short_list, default="N/A")
    print(result2)

    result3 = get_third_element(empty_list, default=0)
    print(result3)