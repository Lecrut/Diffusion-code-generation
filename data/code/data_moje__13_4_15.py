import itertools

def nth_element(stream, n, default=None):
    return next(itertools.islice(stream, n, None), default)

if __name__ == '__main__':
    sample_stream = (x * x for x in range(1, 10))
    target_index = 4
    result = nth_element(sample_stream, target_index)
    print(result)