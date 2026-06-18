def calculate_set_operations(set_x, set_y):
    """
    Calculates intersection, union of two sets and reports size difference.
    
    Args:
        set_x (set or list-like): First input dataset
        set_y (set or list-like): Second input dataset
    
    Returns:
        dict: Contains 'intersection_size', 'union_size', and 'size_difference'
    """
    # Convert inputs to sets if they aren't already
    s1 = set(set_x)
    s2 = set(set_y)
    
    intersection = s1 & s2
    union = s1 | s2
    
    return {
        "intersection_size": len(intersection),
        "union_size": len(union),
        "size_difference": len(union) - len(intersection)
    }

if __name__ == '__main__':
    # Hard-coded sample values (no user input required)
    set_x = [1, 2, 3, 4, 5]
    set_y = [4, 5, 6, 7, 8]
    
    result = calculate_set_operations(set_x, set_y)
    
    print(f"Intersection size: {result['intersection_size']}")
    print(f"Union size: {result['union_size']}")
    print(f"Difference in size (Union - Intersection): {result['size_difference']}")