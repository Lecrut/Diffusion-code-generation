def check_endpoints(iterable):
    if not hasattr(iterable, '__getitem__') or not hasattr(iterable, '__len__'):
        raise TypeError("Input must be an iterable")
    
    if len(iterable) == 0:
        return (None, None)
    
    first = iterable[0]
    last = iterable[-1]
    return (first, last)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(check_endpoints(sample_list))
    empty_list = []
    print(check_endpoints(empty_list))
    single_element = [10]
    print(check_endpoints(single_element))
    string_input = "hello"
    try:
        print(check_endpoints(string_input))
    except TypeError as e:
        print(e)