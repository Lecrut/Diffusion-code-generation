import heapq
THRESHOLD = 1000

def find_median_efficient(data):
    n = len(data)
    if n == 0:
        return None
    min_heap = []
    max_heap = []
    for value in data:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, value))
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
    if n % 2 == 1:
        return min_heap[0]
    else:
        return (min_heap[0] - max_heap[0]) / 2.0
if __name__ == '__main__':
    large_dataset = [random.randint(1, 1000000) for _ in range(1000000)]
    median_value = find_median_efficient(large_dataset)
    print(median_value)