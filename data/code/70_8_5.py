def check_endpoints(iterable):
    try:
        items = list(iterable)
    except TypeError:
        raise ValueError("Input must be an iterable")
    
    if not items:
        return None, None
    
    return items[0], items[-1]

if __name__ == '__main__':
    result = check_endpoints([1, 2, 3])
    print(result)
    
    empty_result = check_endpoints([])
    print(empty_result)
    
    str_result = check_endpoints("abc")
    print(str_result)