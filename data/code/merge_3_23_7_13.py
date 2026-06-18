import sys

def calculate_set_operations(set_x, set_y):
    """
    Calculates intersection and union of two sets and returns their sizes difference.
    
    Parameters:
        set_x (set or list-like): First dataset to process.
        set_y (set or list-like): Second dataset to process.
        
    Returns:
        dict: Contains 'intersection_size', 'union_size', and 'difference'.
              Difference is calculated as union_size - intersection_size.
    
    Raises:
        ValueError: If input types are not hashable/iterable for set conversion or if inputs are None.
    """
    # Ensure sets (convert lists/tuples to sets)
    s_x = set(set_x) if isinstance(set_x, list) else set(x for x in str(set_x))
    try:
        s_y = set(set_y) if isinstance(set_y, list) else set(y for y in str(set_y))
    except TypeError as e:
        raise ValueError(f"Invalid input type for second set: {e}")

    intersection_size = len(s_x & s_y)
    union_size = len(s_x | s_y)
    
    return {
        'intersection_size': intersection_size,
        'union_size': union_size,
        'difference': union_size - intersection_size
    }

if __name__ == '__main__':
    # Hard-coded sample values (no user input required)
    set_x = [10, 20, 30, 40]
    set_y = [30, 40, 50, 60]

    result = calculate_set_operations(set_x, set_y)
    
    print(f"Intersection Size: {result['intersection_size']}")
    print(f"Union Size:        {result['union_size']}")
    print(f"Difference (U - I):{result['difference']}")