import heapq

def find_median(nums):
    if not nums:
        raise ValueError("Input list cannot be empty")
    
    min_heap = []
    max_heap = []
    
    for num in nums:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, num))
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
    
    if len(min_heap) == len(max_heap):
        return (min_heap[0] - max_heap[0]) / 2.0
    else:
        return min_heap[0]

if __name__ == '__main__':
    list1 = [3, 5, 1, 4, 2]
    list2 = [10, 7, 2, 5, 1]
    list3 = [99]
    list4 = []
    print(f"Median of {list1}: {find_median(list1)}")
    print(f"Median of {list2}: {find_median(list2)}")
    print(f"Median of {list3}: {find_median(list3)}")