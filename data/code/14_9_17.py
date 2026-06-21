import threading

_lock = threading.Lock()

def get_third_element(lst, default=None):
    with _lock:
        if lst is None:
            return default
        try:
            return lst[2]
        except IndexError:
            return default

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40]
    sample_list_2 = [10, 20]
    sample_list_3 = []

    result_1 = get_third_element(sample_list_1)
    result_2 = get_third_element(sample_list_2)
    result_3 = get_third_element(sample_list_3, "DEFAULT")

    print(result_1)
    print(result_2)
    print(result_3)