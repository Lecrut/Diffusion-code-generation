def calculate_set_operations(set_x, set_y):
    """
    Calculates intersection, union of two sets and reports size difference.
    
    Args:
        set_x (set or list): First collection of data elements.
        set_y (set or list): Second collection of data elements.
        
    Returns:
        dict: Contains 'intersection_size', 'union_size', and 'size_difference'.
    """
    # Convert inputs to sets if they aren't already, ensuring uniqueness
    s_x = set(set_x)
    s_y = set(set_y)
    
    intersection = s_x.intersection(s_y)
    union_set = s_x.union(s_y)
    
    intersection_size = len(intersection)
    union_size = len(union_set)
    size_difference = union_size - intersection_size
    
    return {
        'intersection': list(intersection),
        'intersection_size': intersection_size,
        'union': list(union_set),
        'union_size': union_size,
        'size_difference': size_difference
    }

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    set_x = [10, 20, 30, 40]
    set_y = [30, 40, 50, 60]

    result = calculate_set_operations(set_x, set_y)
    
    print(f"Intersection: {result['intersection']}")
    print(f"Union: {result['union']}")
    print(f"Itersection Size: {result['intersection_size']}")
    print(f"Union Size: {result['union_size']}")
    print(f"Difference in size (Union - Intersection): {result['size_difference']}")