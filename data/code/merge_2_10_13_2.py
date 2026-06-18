import heapq
def sorted_stream_generator(data_source, condition):
    heap = []
    for item in data_source:
        if condition(item):
            pass
    def _process():
        for item in data_source:
            if condition(item):
                yield item
    sorted_items = []
    for item in _process():
        sorted_items.append(item)
    return (item for item in sorted(sorted_items))
if __name__ == '__main__':
    def is_even(x):
        return x % 2 == 0
    raw_data = [1, 4, 3, 8, 5, 9, 2, 7, 6] 
    result_gen = sorted_stream_generator(raw_data, is_even)
    print(list(result_gen))