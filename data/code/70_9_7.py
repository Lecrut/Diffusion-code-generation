def check_endpoints(iterable):
    if not iterable:
        return (None, None)
    first = iterable[0]
    try:
        last = iterable[-1]
    except IndexError:
        last = None
    return (first, last)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(check_endpoints(sample_list))
    empty_list = []
    print(check_endpoints(empty_list))
    single_element = [10]
    print(check_endpoints(single_element))
    string_sample = "hello"
    print(check_endpoints(string_sample))
    tuple_sample = (1, 2, 3)
    print(check_endpoints(tuple_sample))