def stream_sum(iterable):
    current_sum = 0
    for item in iterable:
        current_sum += item
        yield current_sum
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    result_generator = stream_sum(data)
    final_sum = 0
    print("Running stream_sum on:", data)
    for running_sum in result_generator:
        print("Running sum:", running_sum)
        final_sum = running_sum
    print("Final sum:", final_sum)
    data_empty = []
    result_generator_empty = stream_sum(data_empty)
    print("\nRunning stream_sum on empty list:", data_empty)
    for running_sum in result_generator_empty:
        print("Running sum:", running_sum)