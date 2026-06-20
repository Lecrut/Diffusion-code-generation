def first_last_generator(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return
    last = None
    for item in iterator:
        last = item
    yield first
    if last is not None:
        yield last

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(list(first_last_generator(sample_values)))