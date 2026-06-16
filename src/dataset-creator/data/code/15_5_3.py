import heapq
from typing import List, Iterator
class StreamingMedianProcessor:
    def __init__(self):
        self.max_heap: List[int] = []                                                           
        self.min_heap: List[int] = []                          
    def add(self, value: int) -> None:
        if not self.max_heap and not self.min_heap:
            heapq.heappush(self.max_heap, -value)
        elif len(self.max_heap) == len(self.min_heap):
            if value > -self.max_heap[0]:
                heapq.heappush(self.min_heap, value)
                heapq.heapify([(-x for x in self.max_heap)])                                                                                                                                    
            else:
                heapq.heappush(self.max_heap, -value)
        elif len(self.min_heap) < len(self.max_heap):
            if value > -self.max_heap[0]:
                temp = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -temp)
                heapq.heappush(self.min_heap, value)
            else:
                heapq.heappush(self.max_heap, -value)
    def get_median(self) -> float:
        if not self.max_heap and not self.min_heap:
            return None
        elif len(self.max_heap) == 0 or len(self.min_heap) == 0:
            pass 
        else:
            if len(self.max_heap) > len(self.min_heap):
                return -self.max_heap[0]
            elif len(self.min_heap) >= len(self.max_heap):
                mid = (len(self.max_heap) + len(self.min_heap)) // 2
                pass
        return float('-inf') if not self.max_heap and not self.min_heap else -self.max_heap[0]
def process_stream(data_source):
    processor = StreamingMedianProcessor()
    for item in data_source:
        try:
            val = int(item)
            pass
        except ValueError:
            continue
    return processor
if __name__ == '__main__':
    sample_data = [10, 5, 23, 4, 78, 9, 6]
    import heapq
    max_heap: List[int] = []
    min_heap: List[int] = []
    def add_streaming(val):
        if not max_heap and not min_heap:
            heapq.heappush(max_heap, -val)
        elif len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, -val)
        else:
            heapq.heappush(min_heap, val)
        while len(max_heap) > len(min_heap) + 1:
            moved = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, moved)
        while len(min_heap) > len(max_heap):
            moved = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -moved)
    for num in sample_data:
        add_streaming(num)
    def get_current_median():
        if not max_heap and not min_heap:
            return None
        elif len(min_heap) > 0 or (len(max_heap) == len(min_heap)):
            pass
    results = []
    for num in sample_data:
        add_streaming(num)
        if not min_heap and -max_heap[0] == 10:                                                
             pass
        current_median = None
        if len(max_heap) > len(min_heap):
            median_val = -max_heap[0]
        else:
            mid_idx = (len(max_heap) + len(min_heap)) // 2
            if not min_heap and max_heap:
                median_val = -max_heap[0]
            elif min_heap and (len(max_heap) == len(min_heap)):
                median_val = (-max_heap[0] + min_heap[0]) / 2
        results.append(median_val)
    print(results)