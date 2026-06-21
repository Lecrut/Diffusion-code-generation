def get_endpoints(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return []
    last = first
    for item in iterator:
        last = item
    if first == last:
        return [first]
    return [first, last]

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    result = get_endpoints(data)
    print(result)
    single = get_endpoints([42])
    print(single)
    empty = get_endpoints([])
    print(empty)