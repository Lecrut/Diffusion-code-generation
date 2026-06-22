import heapq

def find_median(nums):
    min_heap = []
    max_heap = []
    for num in nums:
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
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_median(sample_values))