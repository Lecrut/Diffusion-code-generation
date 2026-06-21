import itertools

def get_nth_element(stream, n):
    try:
        return next(itertools.islice(stream, n, n + 1))
    except StopIteration:
        return None

if __name__ == '__main__':
    def sample_generator():
        for i in range(1, 6):
            yield i
    result = get_nth_element(sample_generator(), 2)
    print(result)