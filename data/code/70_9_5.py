def check_endpoints(iterable):
    return iterable[0], iterable[-1] if iterable else (None, None)

if __name__ == '__main__':
    print(check_endpoints([1, 2, 3, 4, 5]))
    print(check_endpoints('hello'))
    print(check_endpoints([]))