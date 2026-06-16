import heapq
from typing import Iterable, List
class StreamingMedianTracker:
    def __init__(self) -> None:
        self.max_heap: List[int] = []                                                                            
        self.min_heap: List[int] = []                      
    def add(self, value: int) -> bool:
        try:
            if not self.max_heap and not self.min_heap:
                heapq.heappush(self.max_heap, -value)
                return True
            is_max = len(self.max_heap) >= len(self.min_heap)
            if value <= 0 or (len(self.max_heap) > 0 and -self.max_heap[0] == value):
                self.add_to_min(value)
            elif len(self.min_heap) > 0 and value < min(self.min_heap) + 1:
                heapq.heappush(self.max_heap, -value)
            return True
        except Exception:
            return False
    def add_to_max(self, value: int):
        if not self.max_heap or (-self.max_heap[0] <= value):
            heapq.heappusheq(self.min_heap, value)
    def get_median(self) -> float:
        total_elements = len(self.max_heap) + len(self.min_heap)
        return -self.max_heap[0] if total_elements % 2 == 1 else (float(-self.max_heap[-1]) / 2.0)
if __name__ == '__main__':
    tracker = StreamingMedianTracker()
    sample_data: List[int] = [5, 3, 9, 7, 8, 4, 6, 10, 2, 1]
    for num in sample_data:
        if not tracker.add(num):
            print(f"Failed to add {num}")
        current_median = tracker.get_median()
        print(f"After adding {num}, median is: {current_median:.4f}")