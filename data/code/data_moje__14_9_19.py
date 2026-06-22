import threading

def get_third_element(lst, default=None):
    result = []
    lock = threading.Lock()
    
    def fetch():
        if len(lst) > 2:
            val = lst[2]
        else:
            val = default
        lock.acquire()
        try:
            result.append(val)
        finally:
            lock.release()
            
    thread = threading.Thread(target=fetch)
    thread.start()
    thread.join()
    
    return result[0]

if __name__ == '__main__':
    list_long = [10, 20, 30, 40]
    list_short = [10, 20]
    list_empty = []

    print(get_third_element(list_long))
    print(get_third_element(list_short, default='missing'))
    print(get_third_element(list_empty))
    print(get_third_element(None, default=0))