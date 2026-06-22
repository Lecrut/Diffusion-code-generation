import heapq

MEDIUM_THRESHOLD = 1000000

def calculate_median(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    n = len(data)
    if n < MEDIUM_THRESHOLD:
        sorted_data = sorted(data)
        if n % 2 == 1:
            return sorted_data[n // 2]
        else:
            mid1 = sorted_data[n // 2 - 1]
            mid2 = sorted_data[n // 2]
            return (mid1 + mid2) / 2.0
    else:
        min_heap, max_heap = [], []
        for num in data:
            if not max_heap or num <= -max_heap[0]:
                heapq.heappush(max_heap, -num)
                if len(max_heap) > len(min_heap) + 1:
                    heapq.heappush(min_heap, -heapq.heappop(max_heap))
            else:
                heapq.heappush(min_heap, num)
                if len(min_heap) > len(max_heap):
                    heapq.heappush(max_heap, -heapq.heappop(min_heap))
        
        if len(max_heap) == len(min_heap):
            return (-max_heap[0] + min_heap[0]) / 2.0
        else:
            return -max_heap[0]

if __name__ == '__main__':
    list1 = [3.5, 1.2, 8.9, 4.1, 2.3]
    list2 = [10.0, 5.0, 2.0, 7.0, 1.0]
    list3 = [5.5]
    list4 = []
    print(f"Median of {list1}: {calculate_median(list1)}")
    print(f"Median of {list2}: {calculate_median(list2)}")
    print(f"Median of {list3}: {calculate_median(list3)}")