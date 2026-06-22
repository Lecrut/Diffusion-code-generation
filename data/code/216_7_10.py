import heapq

def calculate_median(data):
    n = len(data)
    if n == 0:
        raise ValueError("Input list cannot be empty")
    
    min_heap, max_heap = [], []
    for num in data:
        heapq.heappush(min_heap, -heapq.heappushpop(max_heap, -num))
        if len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
    
    if n % 2 == 1:
        return -max_heap[0]
    else:
        return (-max_heap[0] + min_heap[0]) / 2.0

if __name__ == '__main__':
    list1 = [1, 3, 2]
    list2 = [5, 2, 8, 1, 9]
    list3 = [10, 4, 7, 2, 15]
    list4 = []
    list5 = [1, 2, 3, 4, 5, 6]

    print(f"Median of {list1}: {calculate_median(list1)}")
    print(f"Median of {list2}: {calculate_median(list2)}")
    print(f"Median of {list3}: {calculate_median(list3)}")
    print(f"Median of {list4}: {calculate_median(list4)}")
    print(f"Median of {list5}: {calculate_median(list5)}")