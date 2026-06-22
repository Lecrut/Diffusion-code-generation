def check_endpoints(iterable):
    try:
        items = list(iterable)
    except TypeError:
        raise ValueError("Input must be an iterable")
    
    if not items:
        return None, None
    
    return items[0], items[-1]

if __name__ == '__main__':
    test_data = [10, 20, 30, 40, 50]
    print(check_endpoints(test_data))
    
    test_empty = []
    print(check_endpoints(test_empty))
    
    test_string = "Python"
    print(check_endpoints(test_string))