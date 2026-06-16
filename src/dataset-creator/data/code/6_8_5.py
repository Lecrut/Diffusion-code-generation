import threading
from functools import partial
def atomic_compare(value1: int, value2: int) -> bool:
    lock = threading.Lock()
    with lock:
        return value1 > value2
if __name__ == '__main__':
    result = atomic_compare(50, 30)
    print(result)