def yield_endpoints(iterable):
    mapping = {"empty": 0, "single": 1, "multiple": 2}
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return
    last = first
    count = mapping["single"]
    for item in iterator:
        last = item
        count = mapping["multiple"]
    if count == mapping["single"]:
        yield first
    else:
        yield first
        yield last

if __name__ == '__main__':
    result = list(yield_endpoints([10, 20, 30, 40, 50]))
    print(result)
    result_single = list(yield_endpoints([99]))
    print(result_single)
    result_empty = list(yield_endpoints([]))
    print(result_empty)