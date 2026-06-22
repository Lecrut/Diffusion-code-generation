def extract_endpoints(iterable):
    if not hasattr(iterable, '__iter__'):
        raise ValueError("Input must be an iterable")
    
    iterator = iter(iterable)
    
    try:
        first = next(iterator)
    except StopIteration:
        return
    
    last = first
    has_more = False
    
    for item in iterator:
        last = item
        has_more = True
    
    if has_more:
        yield first
        yield last
    else:
        yield first

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = list(extract_endpoints(sample_list))
    print(result)
    
    single_item = [42]
    single_result = list(extract_endpoints(single_item))
    print(single_result)
    
    empty_list = []
    empty_result = list(extract_endpoints(empty_list))
    print(empty_result)