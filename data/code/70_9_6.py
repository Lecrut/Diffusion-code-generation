def check_endpoints(iterable):
    if not iterable:
        return (None, None)
    first = next(iter(iterable))
    last = iterable[-1]
    return (first, last)

if __name__ == '__main__':
    print(check_endpoints([1, 2, 3, 4, 5]))
    print(check_endpoints("hello"))
    print(check_endpoints([]))
    print(check_endpoints((10, 20, 30)))
    print(check_endpoints([99]))