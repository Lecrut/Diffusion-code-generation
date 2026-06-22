def check_endpoints(iterable):
    try:
        first_item = next(iter(iterable))
    except StopIteration:
        return None, None
    
    last_item = first_item
    current_item = first_item
    for current_item in iterable:
        last_item = current_item
    
    return first_item, last_item

if __name__ == '__main__':
    data_sequence = [10, 20, 30, 40, 50]
    endpoints = check_endpoints(data_sequence)
    print(endpoints)
    
    empty_sequence = []
    empty_endpoints = check_endpoints(empty_sequence)
    print(empty_endpoints)
    
    single_item_sequence = [99]
    single_endpoints = check_endpoints(single_item_sequence)
    print(single_endpoints)