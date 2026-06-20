def get_first_and_last(iterable):
    it = iter(iterable)
    try:
        first = next(it)
    except StopIteration:
        return
    last = first
    for item in it:
        last = item
    yield first
    if last is not None:
        yield last
if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]
    print(list(get_first_and_last(data1)))
    data2 = [10]
    print(list(get_first_and_last(data2)))
    data3 = [100]