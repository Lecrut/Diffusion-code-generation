import threading
import time
import queue
def read_file(filename, q):
    with open(filename, 'r') as f:
        for line in f:
            q.put(line)
if __name__ == '__main__':
    file_a = "FileA.txt"
    file_b = "FileB.txt"
    with open(file_a, 'w') as f:
        f.write("A line 1\n")
        f.write("A line 2\n")
        f.write("A line 3\n")
    with open(file_b, 'w') as f:
        f.write("B line 1\n")
        f.write("B line 2\n")
        f.write("B line 3\n")
    queue_a = queue.Queue()
    queue_b = queue.Queue()
    thread_a = threading.Thread(target=read_file, args=(file_a, queue_a))
    thread_b = threading.Thread(target=read_file, args=(file_b, queue_b))
    thread_a.start()
    thread_b.start()
    results = []
    while not (queue_a.empty() and queue_b.empty()):
        try:
            line_a = queue_a.get_nowait()
            line_b = queue_b.get_nowait()
            if line_a:
                results.append(f"A: {line_a}")
            if line_b:
                results.append(f"B: {line_b}")
        except queue.Empty:
            pass
        except Exception:
            break
    thread_a.join()
    thread_b.join()
    for result in results:
        print(result)