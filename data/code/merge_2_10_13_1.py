import heapq
def sorted_stream_generator(data_source, condition):
    heap = []
    for item in data_source:
        if condition(item):
            key = getattr(item, 'value', item)                                            
            heapq.heappush(heap, (-key, item))
    while heap:
        _, item = heapq.heappop(heap)
        yield item
if __name__ == '__main__':
    sample_data = [105, 234, 89, 176, 45] * 100000
    condition_func = lambda x: True
    for item in sample_data:
        if isinstance(item, int):
            print(f"Yielded: {item}")