import heapq

def calculate_median(data):
    n = len(data)
    if n == 0:
        raise ValueError('Input list cannot be empty')
    if n % 2 == 1:
        small_heap, large_heap = ([], [])
        heapq.heapify(small_heap)
        heapq.heapify(large_heap)
        for i, num in enumerate(data):
            if i < n // 2 + 1:
                heapq.heappush(small_heap, -num)
            else:
                heapq.heappush(large_heap, num)
            if len(small_heap) > len(large_heap) + 1:
                heapq.heappush(large_heap, -heapq.heappop(small_heap))
            elif len(large_heap) > len(small_heap):
                heapq.heappush(small_heap, -heapq.heappop(large_heap))
        median = -small_heap[0]
    else:
        small_heap, large_heap = ([], [])
        heapq.heapify(small_heap)
        heapq.heapify(large_heap)
        for i, num in enumerate(data):
            if i < n // 2:
                heapq.heappush(small_heap, -num)
            else:
                heapq.heappush(large_heap, num)
            if len(small_heap) > len(large_heap) + 1:
                heapq.heappush(large_heap, -heapq.heappop(small_heap))
            elif len(large_heap) > len(small_heap):
                heapq.heappush(small_heap, -heapq.heappop(large_heap))
        mid1 = -small_heap[0]
        mid2 = large_heap[0]
        median = (mid1 + mid2) / 2.0
    return median
if __name__ == '__main__':
    list1 = [3, 1, 2, 4, 5]
    list2 = [-10, 4, 6, 1000, 10, 20]
    print(f'Median of {list1}: {calculate_median(list1)}')
    print(f'Median of {list2}: {calculate_median(list2)}')