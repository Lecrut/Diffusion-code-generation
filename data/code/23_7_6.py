def calculate_set_operations(set_x, set_y):
    """
    Calculates intersection and union of two sets (or list-like inputs treated as sets).
    
    Args:
        set_x: First input collection (list or other iterable)
        set_y: Second input collection (list or other iterable)
        
    Returns:
        tuple: (intersection_set, union_set, size_difference)
            - intersection_set: Elements common to both inputs
            - union_set: All unique elements from both inputs
            - size_difference: Size of union minus size of intersection
    """
    # Convert inputs to sets for efficient operations
    set_x = set(set_x)
    set_y = set(set_y)
    
    # Calculate intersection and union
    intersection = set_x.intersection(set_y)
    union = set_x.union(set_y)
    
    # Calculate size difference (Union Size - Intersection Size)
    size_difference = len(union) - len(intersection)
    
    return intersection, union, size_difference

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    set_x_sample = [1, 2, 3, 4, 5]
    set_y_sample = [4, 5, 6, 7, 8]
    
    intersection_result, union_result, diff_size = calculate_set_operations(set_x_sample, set_y_sample)
    
    print("Intersection:", sorted(intersection_result))
    print("Union:", sorted(union_result))
    print(f"Size difference (Union - Intersection): {diff_size}")