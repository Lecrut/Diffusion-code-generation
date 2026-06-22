def extract_boundary_values(iterable):
    if hasattr(iterable, '__len__') and len(iterable) == 0:
        return []
    
    iterator = iter(iterable)
    
    try:
        first_element = next(iterator)
    except StopIteration:
        return []
    
    current_element = first_element
    sequence_length = 1
    
    for value in iterator:
        current_element = value
        sequence_length += 1
    
    if sequence_length == 1:
        return [first_element]
    
    return [first_element, current_element]

if __name__ == '__main__':
    sample_data = ['alpha', 'beta', 'gamma', 'delta']
    boundary_result = extract_boundary_values(sample_data)
    print(boundary_result)
    
    sample_singleton = [100]
    singleton_result = extract_boundary_values(sample_singleton)
    print(singleton_result)
    
    sample_empty = tuple()
    empty_result = extract_boundary_values(sample_empty)
    print(empty_result)