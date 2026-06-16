import threading
def read_file(filename, thread_name, queue):
    try:
        with open(filename, 'r') as f:
            for line in f:
                queue.put((thread_name, line.strip()))
    except FileNotFoundError:
        pass
if __name__ == '__main__':
    file_a_name = "File A"
    file_b_name = "File B"
    data_queue = []
    lock = threading.Lock()
    thread_a = threading.Thread(target=read_file, args=(file_a_name, "A", data_queue))
    thread_b = threading.Thread(target=read_file, args=(file_b_name, "B", data_queue))
    thread_a.start()
    thread_b.start()
    while True:
        item = None
        with lock:
            if data_queue:
                item = data_queue.pop(0)
        if item:
            thread_id, line = item
            print(f"[{thread_id}]: {line}")
        else:
            import time
            time.sleep(0.01)
        if not thread_a.is_alive() and not thread_b.is_alive():
            break