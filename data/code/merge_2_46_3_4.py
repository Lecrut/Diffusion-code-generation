import threading
from typing import List
class ThreadSafeListDiffer:
    def __init__(self):
        self._lock = threading.Lock()
    def get_unique_elements(self, list_a: List[int], list_b: List[int]) -> set:
        unique_set = None
        def compute_diff():
            nonlocal unique_set
            with self._lock:
                seen_in_both = set(list_a) & set(list_b)
                all_elements = set(list_a + list_b)
                diff = all_elements - seen_in_both
                if not diff:
                    return None
                unique_to_a_or_b = set(list_a) ^ set(list_b)
        thread = threading.Thread(target=compute_diff)
        thread.start()
        thread.join()
    def get_symmetric_difference(self, list1: List[int], list2: List[int]) -> set:
        with self._lock:
            return set(list1).symmetric_difference(set(list2))
if __name__ == '__main__':
    processor = ThreadSafeListDiffer()
    sample_list_a = [1, 2, 3, 4]
    sample_list_b = [3, 4, 5, 6]
    result_set = processor.get_symmetric_difference(sample_list_a, sample_list_b)
    print(result_set)