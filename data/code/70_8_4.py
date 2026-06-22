def check_endpoints(iterable):
    try:
        first_element = next(iter(iterable))
    except StopIteration:
        return None, None
    
    last_element = first_element
    last_seen = first_element
    
    for current_element in iterable:
        last_seen = current_element
        last_element = current_element
        
    return first_element, last_element

if __name__ == '__main__':
    test_sequence = "hello"
    start_char, end_char = check_endpoints(test_sequence)
    print(f"Start: {start_char}, End: {end_char}")
    
    test_numbers = [10, 20, 30]
    first_num, last_num = check_endpoints(test_numbers)
    print(f"First: {first_num}, Last: {last_num}")
    
    test_empty = []
    empty_start, empty_end = check_endpoints(test_empty)
    print(f"Empty: {empty_start}, {empty_end}")