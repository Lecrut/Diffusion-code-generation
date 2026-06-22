import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def add_num(self, num: int) -> None:
        if not self.min_heap or num <= -self.min_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            return -self.max_heap[0]
if __name__ == '__main__':
    mf = MedianFinder()
    mf.add_num(1)
    print(mf.find_median())
    mf.add_num(3)
    print(mf.find_median())
    mf.add_num(2)
    print(mf.find_median())