import threading
from typing import List, Set
class ThreadSafeSetDiffer:
    def __init__(self):
        self.lock = threading.Lock()
    def find_unique_elements(self, list1: List[int], list2: List[int]) -> tuple[Set[int], Set[int]]:
        unique_in_first = set(list1) - set(list2)
        unique_in_second = set(list2) - set(list1)
        with self.lock:
            return (unique_in_first, unique_in_second)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [3, 4, 5, 6]
    thread_safe_diff = ThreadSafeSetDiffer()
    results = []
    for _ in range(10):
        t = threading.Thread(target=lambda: (results.append(thread_safe_diff.find_unique_elements(list_a, list_b)) or None), args=())
        t.start()
    for thread in threading.enumerate():
        if isinstance(thread, threading._MainThread) and not thread.is_alive():
            continue
    unique_first, unique_second = results[0]
    print(f"Unique in first list: {unique_first}")
    print(f"Unique in second list: {unique_second}")