def check_endpoints(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        raise ValueError("The provided iterable is empty")
    
    last = first
    for item in iterator:
        last = item
    
    return first, last

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = check_endpoints(sample_list)
    print(result)
    
    sample_string = "Python"
    result_str = check_endpoints(sample_string)
    print(result_str)
    
    sample_tuple = (1, 2, 3)
    result_tuple = check_endpoints(sample_tuple)
    print(result_tuple)