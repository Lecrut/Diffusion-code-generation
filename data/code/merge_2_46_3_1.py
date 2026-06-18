import threading
from typing import List
class ThreadSafeSetDifference:
    def __init__(self):
        self.lock = threading.Lock()
    def find_unique_elements(self, list_a: List[int], list_b: List[int]) -> set:
        unique_set = set(list_a) - set(list_b)
        return unique_set
if __name__ == '__main__':
    thread_safe_diff = ThreadSafeSetDifference()
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = [4, 5, 6, 7, 8]
    result = thread_safe_diff.find_unique_elements(sample_list_1, sample_list_2)
    print(f"Unique elements in list A but not B: {result}")