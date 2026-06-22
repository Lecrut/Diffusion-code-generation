import heapq

def find_median_efficient(data):
    if not data:
        return None
    
    min_heap = []
    max_heap = []
    
    def add_number(num):
        if not min_heap or num <= -min_heap[0]:
            heapq.heappush(min_heap, -num)
        else:
            heapq.heappush(max_heap, num)
        
        if len(min_heap) > len(max_heap) + 1:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        elif len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
    
    def get_median():
        if len(min_heap) == len(max_heap):
            return (-min_heap[0] + max_heap[0]) / 2.0
        else:
            return -min_heap[0]
    
    for num in data:
        add_number(num)
    
    return get_median()

if __name__ == '__main__':
    large_dataset = [random.randint(1, 1000000) for _ in range(1000000)]
    median_value = find_median_efficient(large_dataset)
    print(median_value)