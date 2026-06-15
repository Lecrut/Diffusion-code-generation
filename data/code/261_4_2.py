import heapq
def find_median_iterator(data_iterator):
    heap = []
    for item in data_iterator:
        if len(heap) < 50000:
            heapq.heappush(heap, item)
            heapq.heapify(heap)
        if len(heap) >= 2:
            if len(heap) == 1:
                continue
            if len(heap) % 2 != 0:
                median_low = heap[len(heap) // 2 - 1]
                median_high = heap[len(heap) // 2]
                return (median_low + median_high) / 2.0
            else:
                median_low = heap[len(heap) // 2 - 1]
                median_high = heap[len(heap) // 2]
                return (median_low + median_high) / 2.0
    if not heap:
        return None
    sorted_list = sorted(heap)
    n = len(sorted_list)
    if n % 2 == 1:
        return sorted_list[n // 2]
    else:
        mid1 = sorted_list[n // 2 - 1]
        mid2 = sorted_list[n // 2]
        return (mid1 + mid2) / 2.0
if __name__ == '__main__':
    data_source = (x for x in range(100000))
    median_result = find_median_iterator(data_source)
    print(f"Median: {median_result}")
    data_source_2 = (x for x in range(5))
    median_result_2 = find_median_iterator(data_source_2)
    print(f"Median: {median_result_2}")
    data_source_3 = iter([1, 7, 3, 9, 5])
    median_result_3 = find_median_iterator(data_source_3)
    print(f"Median: {median_result_3}")