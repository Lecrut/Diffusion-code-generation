def calculate_set_operations(set_x, set_y):
    """
    Calculates intersection and union of two sets (passed as lists) 
    and returns their sizes along with the difference in size between union and intersection.
    
    Parameters:
        set_x (list or iterable): First set of data
        set_y (list or iterable): Second set of data
        
    Returns:
        dict: Contains 'intersection_size', 'union_size', and 'size_difference'
              where size_difference = len(union) - len(intersection)
    """
    # Convert inputs to sets if they aren't already
    s_x = set(set_x)
    s_y = set(set_y)
    
    intersection = s_x.intersection(s_y)
    union = s_x.union(s_y)
    
    intersection_size = len(intersection)
    union_size = len(union)
    size_difference = union_size - intersection_size
    
    return {
        'intersection': list(intersection),
        'intersection_size': intersection_size,
        'union': list(union),
        'union_size': union_size,
        'size_difference': size_difference
    }

if __name__ == '__main__':
    # Hard-coded sample values (no user input required)
    set_x = [10, 20, 30, 40]
    set_y = [30, 40, 50, 60]
    
    result = calculate_set_operations(set_x, set_y)
    
    print("Intersection:", result['intersection'])
    print(f"Size of Intersection: {result['intersection_size']}")
    print("Union:", result['union'])
    print(f"Size of Union: {result['union_size']}")
    print(f"Difference in size (Union - Intersection): {result['size_difference']}")