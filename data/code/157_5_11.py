import heapq

class MinHeap:
    def __init__(self, data):
        self.heap = []
        heapq.heapify(self.heap)
        for item in data:
            heapq.heappush(self.heap, item)

    def get_smallest(self):
        return self.heap[0]

if __name__ == '__main__':
    sample_numbers = [3.5, 2.1, 4.8, 1.9, 5.6]
    min_heap = MinHeap(sample_numbers)
    smallest_number = min_heap.get_smallest()
    print(smallest_number)