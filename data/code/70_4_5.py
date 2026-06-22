def get_endpoints(iterable):
    endpoints_map = {"empty": [], "single": 1, "multiple": 2}
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return endpoints_map["empty"]
    last = first
    count = endpoints_map["single"]
    for item in iterator:
        last = item
        count = endpoints_map["multiple"]
    if count == endpoints_map["single"]:
        return [first]
    return [first, last]

if __name__ == '__main__':
    print(get_endpoints([10, 20, 30, 40]))
    print(get_endpoints([99]))
    print(get_endpoints([]))
    print(get_endpoints("python"))