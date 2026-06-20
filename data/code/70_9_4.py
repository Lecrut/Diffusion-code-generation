def check_endpoints(iterable):
    if not iterable:
        return (None, None)
    first = next(iter(iterable))
    last = iterable[-1]
    return (first, last)

if __name__ == '__main__':
    sample_list = ['a', 'b', 'c', 'd']
    print(check_endpoints(sample_list))
    empty_list = []
    print(check_endpoints(empty_list))
    single_element = [42]
    print(check_endpoints(single_element))