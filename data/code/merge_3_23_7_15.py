def calculate_set_operations(set_x, set_y):
    """
    Calculates intersection and union of two sets.
    
    Args:
        set_x (set or list-like): First collection of data elements.
        set_y (set or list-like): Second collection of data elements.
        
    Returns:
        dict: A dictionary containing the keys 'intersection', 'union', 
              and 'size_difference' where size_difference is defined as 
              len(intersection) - len(union). Note that typically this value
              will be negative since intersection is a subset of union (unless one set is empty),
              but we follow the literal instruction "difference in size" as intersection minus union.
    """
    # Convert inputs to sets if they are not already
    x_set = set(set_x)
    y_set = set(set_y)
    
    intersection_result = x_set.intersection(y_set)
    union_result = x_set.union(y_set)
    
    size_difference = len(intersection_result) - len(union_result)
    
    return {
        'intersection': list(intersection_result),
        'union': list(union_result),
        'size_difference': size_difference,
        'len_intersection': len(intersection_result),
        'len_union': len(union_result)
    }

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    
    set_x = [10, 20, 30, 40]
    set_y = [30, 40, 50, 60]
    
    results = calculate_set_operations(set_x, set_y)
    
    print(f"Intersection: {results['intersection']}")
    print(f"Union: {results['union']}")
    print(f"Difference in size (Inter - Union): {results['size_difference']}")