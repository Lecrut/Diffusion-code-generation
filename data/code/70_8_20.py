def _validate_iterable(obj):
    if hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        return True
    if isinstance(obj, (str, bytes, bytearray)):
        return True
    return False

def check_endpoints(iterable):
    if not _validate_iterable(iterable):
        raise ValueError("Input must be an iterable")
    
    try:
        iterator = iter(iterable)
        first = next(iterator)
    except StopIteration:
        return None, None
    
    last = first
    for item in iterator:
        last = item
    
    return first, last

if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50]
    print(check_endpoints(numbers))
    
    empty = []
    print(check_endpoints(empty))
    
    text = "python"
    print(check_endpoints(text))
    
    single = [99]
    print(check_endpoints(single))