import threading
def is_greater_atomic(value1: int, value2: int) -> bool:
    return value1 > value2
if __name__ == '__main__':
    lock = threading.Lock()
    def worker():
        val_a = 50
        val_b = 30
        with lock:
            result = is_greater_atomic(val_a, val_b)
        print(f"Result for {val_a} > {val_b}: {result}")
    threads = []
    for _ in range(10):
        t = threading.Thread(target=worker)
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()