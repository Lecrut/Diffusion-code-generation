import threading
from typing import List, Set
class ThreadSafeSetDiffer:
    def __init__(self):
        self.lock = threading.Lock()
    def find_unique_elements(self, list_a: List[int], list_b: List[int]) -> dict[str, int]:
        unique_in_a_count = 0
        unique_in_b_count = 0
        with self.lock:
            set_a = set(list_a)
            set_b = set(list_b)
            for item in set_a:
                if item not in set_b:
                    unique_in_a_count += 1
            for item in set_b:
                if item not in set_a:
                    unique_in_b_count += 1
        return {
            "unique_to_list_a": list(set(list_a) - set(list_b)),
            "unique_to_list_b": list(set(list_b) - set(list_a))
        }
if __name__ == '__main__':
    thread_safe_differ = ThreadSafeSetDiffer()
    sample_list_1: List[int] = [1, 2, 3, 4, 5]
    sample_list_2: List[int] = [4, 5, 6, 7, 8]
    result = thread_safe_differ.find_unique_elements(sample_list_1, sample_list_2)
    print(f"Unique in first list: {result['unique_to_list_a']}")
    print(f"Unique in second list: {result['unique_to_list_b']}")