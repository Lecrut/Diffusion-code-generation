def get_endpoints(iterable):
    it = iter(iterable)
    try:
        first = next(it)
    except StopIteration:
        return []
    last = first
    for item in it:
        last = item
    if first is last:
        return [first]
    return [first, last]

if __name__ == '__main__':
    print(get_endpoints([10, 20, 30]))
    print(get_endpoints([42]))
    print(get_endpoints([]))