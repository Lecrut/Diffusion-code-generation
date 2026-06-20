def check_endpoints(iterable):
    if not hasattr(iterable, '__iter__'):
        raise TypeError("Input must be an iterable")
    try:
        first = next(iter(iterable))
    except StopIteration:
        return (None, None)
    last = iterable[-1]
    return (first, last)

if __name__ == '__main__':
    print(check_endpoints([1, 2, 3, 4, 5]))
    print(check_endpoints("hello"))
    print(check_endpoints([]))
    print(check_endpoints((10, 20, 30)))
    print(check_endpoints({1, 2, 3}))