import heapq

def find_median_efficient(data):
    if not data:
        raise ValueError("Data cannot be empty")
    
    min_heap = []
    max_heap = []
    
    for value in data:
        if len(min_heap) == len(max_heap):
            heapq.heappush(max_heap, -heapq.heappushpop(min_heap, value))
        else:
            heapq.heappush(min_heap, -heapq.heappushpop(max_heap, -value))
    
    if len(min_heap) > len(max_heap):
        return min_heap[0]
    else:
        return (-max_heap[0] + min_heap[0]) / 2.0

if __name__ == '__main__':
    large_dataset = [random.randint(1, 1000000) for _ in range(1000000)]
    median_value = find_median_efficient(large_dataset)
    print(median_value)