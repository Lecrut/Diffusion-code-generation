import threading
from concurrent.futures import ThreadPoolExecutor
class AtomicComparator:
    def __init__(self):
        self.lock = threading.Lock()
    def exceeds(self, value1, value2):
        with self.lock:
            return value1 > value2
def compare_values(value1, value2):
    comparator = AtomicComparator()
    result = False
    def worker():
        nonlocal result
        if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
            raise TypeError("Values must be numeric")
        with ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(comparator.exceeds, value1, value2)
            result = future.result()
    worker()
    return result
if __name__ == '__main__':
    val_a = 45.67890123456789
    val_b = -1
    if compare_values(val_a, val_b):
        print("Value A exceeds Value B")
    else:
        print("Value A does not exceed Value B")