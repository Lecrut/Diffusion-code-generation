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
        f.write("Line A1\n")
        f.write("Line A2\n")
        f.write("Line A3\n")
    with open(file_b, 'w') as f:
        f.write("Line B1\n")
        f.write("Line B2\n")
        f.write("Line B3\n")
    queue_a = queue.Queue()
    queue_b = queue.Queue()
    thread_a = threading.Thread(target=read_file, args=(file_a, queue_a))
    thread_b = threading.Thread(target=read_file, args=(file_b, queue_b))
    thread_a.start()
    thread_b.start()
    print("Interleaved output:")
    while not queue_a.empty() or not queue_b.empty():
        if not queue_a.empty():
            print(queue_a.get())
        if not queue_b.empty():
            print(queue_b.get())
    thread_a.join()
    thread_b.join()