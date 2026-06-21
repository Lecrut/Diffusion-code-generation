import itertools

def get_nth_element(stream, n):
    return next(itertools.islice(stream, n, None))

if __name__ == '__main__':
    sample_stream = (x * x for x in range(10))
    n = 4
    result = get_nth_element(sample_stream, n)
    print(result)