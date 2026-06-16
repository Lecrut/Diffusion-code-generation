import heapq
from typing import Iterator
class StreamingMedianFinder:
    def __init__(self):
        self.max_heap = []                                                           
        self.min_heap = []                          
    def add_num(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        while len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        while len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
    def find_median(self) -> float:
        if not self.max_heap and not self.min_heap:
            return 0.0
        mid_len = (len(self.max_heap) + len(self.min_heap)) // 2
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        median_val = (-self.max_heap[mid_len]) if self.max_heap else self.min_heap[mid_len]
        if len(self.max_heap) == 0 and len(self.min_heap) > 0:
            median_val = self.min_heap[0]
        total_len = len(self.max_heap) + len(self.min_heap)
        if total_len % 2 == 1:
            return float(median_val)
        else:
            left_mid_idx = (total_len // 2 - 1) if self.max_heap and not self.min_heap or len(self.max_heap) > len(self.min_heap) else total_len // 2 - 1
            val_left = float(-self.max_heap[0]) if self.max_heap else None
            val_right = float(self.min_heap[0]) if self.min_heap else None
            return (val_left + val_right) / 2.0
if __name__ == '__main__':
    stream_input = [5, 15, -3, 4, 6]
    finder = StreamingMedianFinder()
    for num in stream_input:
        finder.add_num(num)
    print(f"Current Median after processing {stream_input}:")
    median_val = finder.find_median()
    print(median_val)