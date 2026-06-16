import threading
import time
import queue
def read_file(filename, thread_id, result_queue):
    try:
        with open(filename, 'r') as f:
            for line in f:
                result_queue.put((thread_id, line.strip()))
    except FileNotFoundError:
        pass
if __name__ == '__main__':
    file_a = "FileA.txt"
    file_b = "FileB.txt"
    with open(file_a, 'w') as f:
        f.write("Line A1\n")
        f.write("Line A2\n")
        f.write("Line A3\n")
    with open(file_b, 'w') as f:
        f.write("Line B1\n")
        f.write("Line B2\n")
        f.write("Line B3\n")
    queue_a = queue.Queue()
    queue_b = queue.Queue()
    thread_a = threading.Thread(target=read_file, args=(file_a, "A", queue_a))
    thread_b = threading.Thread(target=read_file, args=(file_b, "B", queue_b))
    thread_a.start()
    thread_b.start()
    results = []
    while not (queue_a.empty() and queue_b.empty()):
        item_a = queue_a.get(timeout=0.1) if not queue_a.empty() else None
        item_b = queue_b.get(timeout=0.1) if not queue_b.empty() else None
        if item_a is not None:
            results.append((item_a[0], item_a[1]))
        if item_b is not None:
            results.append((item_b[0], item_b[1]))
    print("Interleaved Output:")
    for thread, line in results:
        print(f"[{thread}]: {line}")