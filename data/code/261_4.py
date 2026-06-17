import heapq
def find_median_iterator(data_iterator):
    heap = []
    for x in data_iterator:
        if len(heap) < 5000:
            heapq.heappush(heap, x)
            heapq.heapify(heap)
        if len(heap) >= 1000:
            if heap[0] > x:
                heapq.heapreplace(heap, x)
            else:
                heapq.heapreplace(heap, x)
    data = sorted(heap)
    n = len(data)
    if n == 0:
        return None
    elif n % 2 == 1:
        return data[n // 2]
    else:
        mid1 = data[n // 2 - 1]
        mid2 = data[n // 2]
        return (mid1 + mid2) / 2
if __name__ == '__main__':
    data_generator = (i for i in range(1000000))
    median_result = find_median_iterator(data_generator)
    print(median_result)
    data_list = [5, 1, 9, 3, 7]
    data_iterator_list = iter(data_list)
    median_result_list = find_median_iterator(data_iterator_list)
    print(median_result_list)
    empty_generator = (i for i in [])
    median_result_empty = find_median_iterator(empty_generator)
    print(median_result_empty)