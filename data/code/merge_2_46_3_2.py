import threading
from typing import List
class ThreadSafeSetDifference:
    def __init__(self):
        self.lock = threading.Lock()
    def compute_difference(self, list_a: List[int], list_b: List[int]) -> set:
        unique_elements = set(list_a) - set(list_b)
        return unique_elements
if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4]
    sample_list_2 = [3, 4, 5, 6]
    thread_safe_processor = ThreadSafeSetDifference()
    with thread_safe_processor.lock:
        result_set = thread_safe_processor.compute_difference(sample_list_1, sample_list_2)
    print(f"Unique elements in list A but not B: {result_set}")