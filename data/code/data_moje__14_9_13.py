import threading

_lock = threading.Lock()

def get_third_element_safe(data, default=None):
    with _lock:
        if len(data) >= 3:
            return data[2]
        return default

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result1 = get_third_element_safe(sample_list)
    print(result1)

    short_list = [1, 2]
    result2 = get_third_element_safe(short_list, default="N/A")
    print(result2)

    empty_list = []
    result3 = get_third_element_safe(empty_list, default=0)
    print(result3)

    single_list = [42]
    result4 = get_third_element_safe(single_list)
    print(result4)