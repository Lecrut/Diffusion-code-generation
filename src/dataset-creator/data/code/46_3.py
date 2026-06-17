import threading
from typing import List, Set
class ThreadSafeUniqueFinder:
    def __init__(self):
        self._lock = threading.Lock()
    def find_unique_elements(self, list_a: List[int], list_b: List[int]) -> tuple[Set[int], Set[int]]:
        unique_in_first: Set[int] = set(list_a) - set(list_b)
        unique_in_second: Set[int] = set(list_b) - set(list_a)
        with self._lock:
            return (unique_in_first, unique_in_second)
if __name__ == '__main__':
    finder = ThreadSafeUniqueFinder()
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result_a, result_b = finder.find_unique_elements(list1, list2)
    print(f"Elements in first only: {result_a}")
    print(f"Elements in second only: {result_b}")