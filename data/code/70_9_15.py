def check_endpoints(iterable):
    if not iterable:
        return (None, None)
    endpoints = {}
    endpoints['first'] = next(iter(iterable))
    endpoints['last'] = iterable[-1]
    return (endpoints['first'], endpoints['last'])

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(check_endpoints(sample_list))
    empty_list = []
    print(check_endpoints(empty_list))