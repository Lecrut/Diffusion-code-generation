import heapq

def find_median_efficient(data):
    min_heap = []
    max_heap = []
    for num in data:
        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
    if len(max_heap) == len(min_heap):
        return (-max_heap[0] + min_heap[0]) / 2.0
    else:
        return -max_heap[0]
if __name__ == '__main__':
    large_dataset = [random.randint(1, 1000000) for _ in range(1000000)]
    median_value = find_median_efficient(large_dataset)
    print(median_value)