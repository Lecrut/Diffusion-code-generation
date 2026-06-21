import threading

_lock = threading.Lock()

def safe_get_third(lst, default=None):
    with _lock:
        if lst is None:
            return default
        try:
            return lst[2]
        except (IndexError, TypeError):
            return default

if __name__ == '__main__':
    list1 = [10, 20, 30, 40]
    list2 = [10, 20]
    list3 = []
    list4 = None

    result1 = safe_get_third(list1)
    result2 = safe_get_third(list2)
    result3 = safe_get_third(list3, default="empty")
    result4 = safe_get_third(list4)

    print(result1)
    print(result2)
    print(result3)
    print(result4)