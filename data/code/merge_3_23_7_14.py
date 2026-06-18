def calculate_set_operations(set_x, set_y):
    """
    Calculates intersection, union, and their size difference.
    
    Parameters:
        set_x (set or list): First input collection of elements.
        set_y (set or list): Second input collection of elements.
        
    Returns:
        dict: A dictionary containing 'intersection', 'union', 
              'intersection_size', 'union_size', and 'difference'.
    """
    # Ensure inputs are sets for efficient operations
    s_x = set(set_x)
    s_y = set(set_y)

    intersection = s_x.intersection(s_y)
    union_set = s_x.union(s_y)

    diff = len(union_set) - len(intersection)

    return {
        'intersection': list(intersection),
        'union': list(union_set),
        'intersection_size': len(intersection),
        'union_size': len(union_set),
        'difference': diff
    }

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, files, or network)
    sample_x = [1, 2, 3, 4]
    sample_y = [3, 4, 5, 6]

    result = calculate_set_operations(sample_x, sample_y)

    print("Set Intersection:", result['intersection'])
    print(f"Intersection Size: {result['intersection_size']}")
    
    print("\nSet Union:", result['union'])
    print(f"Union Size: {result['union_size']}")
    
    print(f"\nDifference in size (Union - Intersection): {result['difference']}")