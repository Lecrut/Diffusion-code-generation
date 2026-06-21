def check_endpoints(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        raise ValueError("Empty iterable")
    
    last = first
    for item in iterator:
        last = item
    return first, last

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = check_endpoints(sample_list)
    print(result)
    
    sample_string = "hello"
    result_str = check_endpoints(sample_string)
    print(result_str)
    
    sample_tuple = (10, 20, 30)
    result_tuple = check_endpoints(sample_tuple)
    print(result_tuple)
    
    try:
        check_endpoints([])
    except ValueError as e:
        print(f"Caught expected error: {e}")