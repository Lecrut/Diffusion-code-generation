import heapq
def sort_by_sign(numbers):
    pos_heap = []
    neg_heap = []
    for num in numbers:
        if num > 0:
            heapq.heappush(pos_heap, -num)                                                                                 
        else:
            heapq.heappush(neg_heap, num)
    sorted_list = []
    while pos_heap:
        val = -heapq.heappop(pos_heap)
        sorted_list.append(val)
    while neg_heap:
        val = heapq.heappop(neg_heap)
        sorted_list.append(val)
    return sorted_list
if __name__ == '__main__':
    sample_data = [3, -1, 4, -7, 0, 2, -5]
    result = sort_by_sign(sample_data)
    print(result)