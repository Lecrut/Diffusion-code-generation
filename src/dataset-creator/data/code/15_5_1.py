import heapq
from typing import List, Iterator, Generator
class StreamingMedianProcessor:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []                                                           
    def add(self, value: int) -> None:
        if not self.min_heap and not self.max_heap:
            heapq.heappush(self.max_heap, -value)
        elif len(self.max_heap) == len(self.min_heap):
            if -self.max_heap[0] < value:
                heapq.heapreplace(self.max_heap, -value)
            else:
                heapq.heappush(self.min_heap, value)
        else:
            if self.min_heap and value > self.min_heap[0]:
                heapq.heapreplace(self.min_heap, value)
            else:
                heapq.heappush(self.max_heap, -value)
    def get_median(self) -> float:
        total_len = len(self.min_heap) + len(self.max_heap)
        if total_len == 0:
            return None
        mid_idx = total_len // 2
        while not self.max_heap and self.min_heap:
            heapq.heappush(self.max_heap, -self.min_heap[0])
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        elif total_len % 2 == 1:
            return float(-self.max_heap[0])
        else:
            mid_min = self.min_heap[mid_idx]
            mid_max = -self.max_heap[mid_idx] if len(self.max_heap) > 0 else None
            while not self.max_heap and self.min_heap:
                heapq.heappush(self.max_heap, -self.min_heap[0])
            return (float(-self.max_heap[-1]) + float(mid_min)) / 2 if mid_max is None else (mid_max + mid_min) / 2
def process_stream(data_source: Iterator[int], output_interval: int = 5):
    processor = StreamingMedianProcessor()
    for i, value in enumerate(data_source):
        processor.add(value)
        if (i + 1) % output_interval == 0 or len(processor.min_heap) > 5:
            yield f"Current Median after {len(processor.max_heap) + len(processor.min_heap)} elements: {processor.get_median()}"
if __name__ == '__main__':
    stream_data = [12, 5, 8, 9, 7, 6, 4, 3, 10, 15, 2, 1]
    results = list(process_stream(iter(stream_data)))
    print("Streaming Median Results:")
    for result in results:
        print(result)