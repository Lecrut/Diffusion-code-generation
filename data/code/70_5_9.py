def first_last_generator(iterable):
    first = next(iter(iterable), None)
    last = None
    for item in iterable:
        last = item
    yield first
    if last is not None:
        yield last

if __name__ == '__main__':
    sample_iterable = [1, 2, 3, 4, 5]
    print(list(first_last_generator(sample_iterable)))