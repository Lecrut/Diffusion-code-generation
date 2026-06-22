import itertools

def nth_element(stream, n, default=None):
    return next(itertools.islice(stream, n, None), default)

if __name__ == "__main__":
    sample_stream = (x for x in range(10))
    n = 3
    result = nth_element(sample_stream, n, default="Not Found")
    print(result)