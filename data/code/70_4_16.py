def get_endpoints(iterable):
    it = iter(iterable)
    try:
        first = next(it)
    except StopIteration:
        return []
    last = first
    found_second = False
    for item in it:
        last = item
        found_second = True
    if found_second:
        return [first, last]
    return [first]

if __name__ == '__main__':
    print(get_endpoints([1, 2, 3, 4, 5]))
    print(get_endpoints([42]))
    print(get_endpoints([]))