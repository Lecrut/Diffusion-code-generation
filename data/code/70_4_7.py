def first_and_last(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return
    last = first
    for item in iterator:
        last = item
    yield first
    yield last

if __name__ == '__main__':
    result = list(first_and_last([1, 2, 3, 4, 5]))
    print(result)