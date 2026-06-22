import heapq

class MedianCalculator:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def add_number(self, number):
        if not self.max_heap or number <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -number)
        else:
            heapq.heappush(self.min_heap, number)
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def get_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            return -self.max_heap[0]
if __name__ == '__main__':
    calculator = MedianCalculator()
    calculator.add_number(3)
    calculator.add_number(1)
    calculator.add_number(8)
    calculator.add_number(4)
    calculator.add_number(2)
    print(f'Median: {calculator.get_median()}')