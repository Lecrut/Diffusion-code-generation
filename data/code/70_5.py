def get_first_and_last(iterable):
    it = iter(iterable)
    try:
        first = next(it)
    except StopIteration:
        return
    last = None
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
    print(list(get_first_and_last(data3)))
    data4 = []
    print(list(get_first_and_last(data4)))
    data5 = ['a', 'b', 'c']
    print(list(get_first_and_last(data5)))
    data6 = [99]
    print(list(get_first_and_last(data6)))