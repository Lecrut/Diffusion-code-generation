import heapq
def sorted_stream_generator(data_source, condition):
    heap = []
    for item in data_source:
        if condition(item):
            heapq.heappush(heap, (-item, id(item)))
            yield -heap[0][0]
def main():
    sample_data = [5, 3, 8, 12, 7, 2, 9, 4, 6, 10]
    def condition(x):
        return x > 3
    result_generator = sorted_stream_generator(sample_data, condition)
    for item in result_generator:
        print(item)
if __name__ == '__main__':
    main()