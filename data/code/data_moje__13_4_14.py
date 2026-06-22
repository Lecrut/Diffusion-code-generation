import itertools

def get_nth_element(stream, n):
    try:
        return next(itertools.islice(stream, n, n + 1))
    except StopIteration:
        return None

if __name__ == '__main__':
    sample_generator = (x * 2 for x in range(10))
    index = 5
    result = get_nth_element(sample_generator, index)
    print(result)