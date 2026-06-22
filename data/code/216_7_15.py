import heapq

def calculate_median(data):
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
    list1 = [3, 1, 2]
    list2 = [9, 5, 8, 1, 7]
    list3 = [15, 4, 7, 2, 10]
    list4 = []
    list5 = [6, 2, 3, 4, 5, 1]

    print(f"Median of {list1}: {calculate_median(list1)}")
    print(f"Median of {list2}: {calculate_median(list2)}")
    print(f"Median of {list3}: {calculate_median(list3)}")
    try:
        print(f"Median of {list4}: {calculate_median(list4)}")
    except ValueError as e:
        print(e)
    print(f"Median of {list5}: {calculate_median(list5)}")