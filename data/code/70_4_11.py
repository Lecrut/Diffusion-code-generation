def get_endpoints(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        raise ValueError("Input iterable is empty")
    
    last = first
    count = 1
    
    for item in iterator:
        last = item
        count += 1
        
    if count == 1:
        return [first]
    return [first, last]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_endpoints(sample_list)
    print(result)
    
    sample_single = [42]
    result_single = get_endpoints(sample_single)
    print(result_single)
    
    try:
        get_endpoints([])
    except ValueError as e:
        print(f"Caught expected error: {e}")