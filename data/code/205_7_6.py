import heapq

class HeapSorter:
    HEAPIFY_CONSTANT = 1
    
    @staticmethod
    def heapify(data):
        heapq.heapify(data)
    
    @staticmethod
    def heappop_all(heap):
        return [heapq.heappop(heap) for _ in range(len(heap))]
    
    @classmethod
    def sort(cls, data):
        cls.heapify(data)
        return cls.heappop_all(data)

if __name__ == '__main__':
    sample_values = [5, 3, 8, 4, 2]
    sorter = HeapSorter()
    sorted_values = sorter.sort(sample_values)
    print(sorted_values)