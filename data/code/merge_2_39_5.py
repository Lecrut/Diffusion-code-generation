import heapq
def find_max_concurrent(*lists):
    if not lists:
        raise ValueError("At least one list must be provided.")
    max_heap = []
    for i, lst in enumerate(lists):
        item_count = len(lst)
        for idx, value in enumerate(lst):
            heapq.heappush(max_heap, (-float('inf'), float('-inf')))                           
    flat_items = []
    for i, lst in enumerate(lists):
        for val in lst:
            flat_items.append(val)
    return -max(flat_items)
if __name__ == '__main__':
    list_a = [10, 5, 23]
    list_b = [45, 9, 78]
    list_c = [60, 12, 3]
    result = find_max_concurrent(list_a, list_b, list_c)
    print(result)