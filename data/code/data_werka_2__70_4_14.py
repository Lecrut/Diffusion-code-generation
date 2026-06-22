def extract_endpoints(iterable):
    ITER_START = 0
    ITER_END = -1
    SINGLE_ITEM_THRESHOLD = 1

    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return []

    last = first
    item_count = 1

    for item in iterator:
        last = item
        item_count += 1

    if item_count == SINGLE_ITEM_THRESHOLD:
        return [first]

    return [first, last]

if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50]
    print(extract_endpoints(numbers))
    print(extract_endpoints([42]))
    print(extract_endpoints([]))
    print(extract_endpoints("hello"))