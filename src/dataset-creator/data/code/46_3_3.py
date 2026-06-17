import threading
from typing import List, Set
class ThreadSafeSetDifference:
    def __init__(self):
        self.lock = threading.Lock()
    def find_unique_elements(self, list_a: List[int], list_b: List[int]) -> int:
        unique_count = 0
        with self.lock:
            set_a = set(list_a)
            for item in list_b:
                if item not in set_a:
                    unique_count += 1
        return unique_count
if __name__ == '__main__':
    thread_safe_set_diff = ThreadSafeSetDifference()
    sample_list_1 = [1, 2, 3, 4]
    sample_list_2 = [3, 4, 5, 6]
    result = thread_safe_set_diff.find_unique_elements(sample_list_1, sample_list_2)
    print(result)