import threading
def append_element(iterable: list) -> None:
    if not isinstance(iterable, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    lock = threading.Lock()
    def safe_append():
        with lock:
            iterable.append(42)
    thread = threading.Thread(target=safe_append)
    thread.start()
    thread.join()
if __name__ == '__main__':
    data_list = [1, 2, 3]
    append_element(data_list)
    print(f"Updated list: {data_list}")