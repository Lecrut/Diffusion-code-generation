def stream_sum(iterable):
    current_sum = 0
    for item in iterable:
        current_sum += item
        yield current_sum
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    result_generator = stream_sum(data)
    final_sum = 0
    print("Stream sum of data:", list(result_generator))
    for s in result_generator:
        final_sum += s
    print("Total sum calculated:", final_sum)