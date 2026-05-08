def stream_sum(iterable):
    current_sum = 0
    for item in iterable:
        current_sum += item
        yield current_sum
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    result_generator = stream_sum(data)
    print(list(result_generator))