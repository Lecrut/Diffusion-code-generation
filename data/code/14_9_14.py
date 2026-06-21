import threading

lock = threading.Lock()

def get_third_element(lst, default=None):
    with lock:
        if len(lst) > 2:
            return lst[2]
        return default

if __name__ == '__main__':
    sample_list_short = [1, 2]
    sample_list_long = [10, 20, 30, 40]

    result_short = get_third_element(sample_list_short)
    result_long = get_third_element(sample_list_long)

    print(result_short)
    print(result_long)