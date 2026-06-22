import heapq

def find_median(data):
    if not data:
        raise ValueError('Input list cannot be empty')
    n = len(data)
    min_heap, max_heap = ([], [])
    for number in data:
        if not max_heap or number < -max_heap[0]:
            heapq.heappush(max_heap, -number)
        else:
            heapq.heappush(min_heap, number)
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
    if n % 2 == 1:
        return -max_heap[0]
    else:
        return (-max_heap[0] + min_heap[0]) / 2.0
if __name__ == '__main__':
    list1 = [3, 1, 2]
    list2 = [5, 2, 8, 1, 9]
    list3 = [10, 4, 7, 2, 15]
    list4 = []
    print(f'Median of {list1}: {find_median(list1)}')
    print(f'Median of {list2}: {find_median(list2)}')
    print(f'Median of {list3}: {find_median(list3)}')