def calculate_set_operations(set_x, set_y):
    """
    Calculates the intersection and union of two sets (or list-like inputs converted to sets),
    compares their sizes, and returns the difference in size.

    Args:
        set_x (list or any iterable): First set of data.
        set_y (list or any iterable): Second set of data.

    Returns:
        dict: A dictionary containing 'intersection_size', 'union_size', 
              and 'size_difference'.
    """
    # Convert inputs to sets if they are not already, ensuring uniqueness
    s_x = set(set_x)
    s_y = set(set_y)

    intersection = s_x.intersection(s_y)
    union_set = s_x.union(s_y)

    intersection_size = len(intersection)
    union_size = len(union_set)
    
    # The difference in size (Union - Intersection is typically the symmetric difference count, 
    # but here we strictly follow "difference in size" as Union Size minus Intersection Size).
    diff_in_size = union_size - intersection_size

    return {
        'intersection': list(intersection),
        'union': list(union_set),
        'intersection_size': intersection_size,
        'union_size': union_size,
        'size_difference': diff_in_size
    }

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    set_x = [10, 20, 30, 40]
    set_y = [30, 40, 50, 60]

    result = calculate_set_operations(set_x, set_y)

    print("Intersection:", result['intersection'])
    print("Union:", result['union'])
    print(f"Size of Intersection: {result['intersection_size']}")
    print(f"Size of Union: {result['union_size']}")
    print(f"Difference in Size (Union - Intersection): {result['size_difference']}")