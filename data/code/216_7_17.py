import heapq

def find_median(data):
    n = len(data)
    if n == 0:
        raise ValueError("Input list cannot be empty")
    
    min_heap, max_heap = [], []
    for num in data:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, num))
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
    
    if n % 2 == 1:
        return min_heap[0]
    else:
        return (min_heap[0] - max_heap[0]) / 2.0

if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    list2 = [5, 2, 8, 1, 9]
    list3 = [10, 4, 7, 2, 15]
    list4 = []
    
    print(f"Median of {list1}: {find_median(list1)}")
    print(f"Median of {list2}: {find_median(list2)}")
    print(f"Median of {list3}: {find_median(list3)}")
    try:
        print(find_median(list4))
    except ValueError as e:
        print(e)