def check_endpoints(iterable):
    if not iterable:
        return (None, None)
    first = iterable[0]
    last = iterable[-1]
    return (first, last)

if __name__ == '__main__':
    print(check_endpoints([1, 2, 3, 4, 5]))
    print(check_endpoints("hello"))
    print(check_endpoints([]))
    print(check_endpoints((10,)))