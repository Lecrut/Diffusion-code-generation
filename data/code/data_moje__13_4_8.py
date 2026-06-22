import itertools

def get_nth_element(stream, n):
    try:
        return next(itertools.islice(stream, n, None))
    except StopIteration:
        raise IndexError("Index out of range")

if __name__ == '__main__':
    sample_stream = (x * 2 for x in range(10))
    result = get_nth_element(sample_stream, 5)
    print(result)