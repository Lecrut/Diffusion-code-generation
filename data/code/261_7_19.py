import heapq

def find_median_efficient(data):
    if not data:
        raise ValueError("Input data cannot be empty")
    
    max_heap = []
    min_heap = []
    median = None
    
    for num in data:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, num))
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        
        if len(max_heap) == len(min_heap):
            median = (-max_heap[0] + min_heap[0]) / 2.0
        else:
            median = min_heap[0]
    
    return median

if __name__ == '__main__':
    large_dataset = [random.randint(1, 1000000) for _ in range(1000000)]
    median_value = find_median_efficient(large_dataset)
    print(median_value)