import threading
from typing import List, Optional, Any
class ThreadSafeMiddleFinder:
    def __init__(self):
        self._lock = threading.Lock()
    def find_middle(self, data: List[Any]) -> Optional[int]:
        if not data:
            return None
        with self._lock:
            n = len(data)
            mid_index = (n - 1) // 2
            return mid_index
def main():
    sample_data: List[int] = [10, 50, 30, 20, 80, 40, 60]
    finder = ThreadSafeMiddleFinder()
    middle_position = finder.find_middle(sample_data)
    print(f"Sample data length: {len(sample_data)}")
    print(f"Calculated middle position index: {middle_position}")
if __name__ == '__main__':
    main()