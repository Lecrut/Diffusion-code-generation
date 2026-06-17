import heapq
def find_max_across_lists(*lists):
    if not any(lists):
        raise ValueError("At least one list must be provided.")
    max_heap = []
    for lst in lists:
        if not isinstance(lst, (list, tuple)):
            continue
        for item in lst:
            heapq.heappush(max_heap, (-item))                               
    return -max_heap[0]
if __name__ == '__main__':
    list_a = [10, 5, 23]
    list_b = [45, 9, 78]
    list_c = [60, 12, 34]
    result = find_max_across_lists(list_a, list_b, list_c)
    print(result)