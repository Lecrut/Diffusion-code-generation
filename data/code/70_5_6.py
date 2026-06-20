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
    data1 = [1, 2, 3, 4, 5]
    print(list(first_last_generator(data1)))
    data2 = [10]
    print(list(first_last_generator(data2)))
    data3 = []
    print(list(first_last_generator(data3)))