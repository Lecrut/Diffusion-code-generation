import heapq

def calculate_median(data):
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
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(calculate_median(sample_data))