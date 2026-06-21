def get_first_and_last(iterable):
    if hasattr(iterable, '__len__') and len(iterable) == 0:
        return []
    
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return []
    
    last = first
    count = 1
    
    for item in iterator:
        last = item
        count += 1
    
    if count == 1:
        return [first]
    
    return [first, last]

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    print(get_first_and_last(data))
    single = [99]
    print(get_first_and_last(single))
    empty = []
    print(get_first_and_last(empty))