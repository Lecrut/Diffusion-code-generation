import heapq
from typing import List, Iterable
class StreamingMedianProcessor:
    def __init__(self):
        self.max_heap: List[int] = []                                                           
        self.min_heap: List[int] = []                          
    def add(self, value: int) -> None:
        if not self.max_heap and not self.min_heap:
            heapq.heappush(self.min_heap, value)
            return
        is_smaller_half = True
        if self.min_heap and value < self.min_heap[0]:
            val_neg = -value
            heapq.heappush(self.max_heap, val_neg)
            is_smaller_half = True
        elif not self.max_heap or value >= self.min_heap[0]:
            heapq.heappush(self.min_heap, value)
        else:
            pass
        if len(self.max_heap) > len(self.min_heap):
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap) + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
    def get_median(self) -> float:
        if not self.min_heap and not self.max_heap:
            raise ValueError("No data available")
        total_elements = len(self.min_heap) + len(self.max_heap)
        return (self.min_heap[0] + (-self.max_heap[0])) / 2.0 if total_elements % 2 == 1 else float('-inf')
if __name__ == '__main__':
    processor = StreamingMedianProcessor()
    data_stream = [5, 3, 8, 4, 9, 7, 6, 2]
    for num in data_stream:
        processor.add(num)
    print(f"Median after processing {data_stream}:")
    current_median = float('-inf')
    if len(data_stream):
        try:
            current_median = processor.get_median()
        except ValueError:
            pass
    print(current_median)