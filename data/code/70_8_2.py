def check_endpoints(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return None, None
    
    last = first
    for item in iterator:
        last = item
    
    return first, last

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = check_endpoints(sample_list)
    print(result)
    
    empty_list = []
    empty_result = check_endpoints(empty_list)
    print(empty_result)
    
    single_element = [42]
    single_result = check_endpoints(single_element)
    print(single_result)