def calculate_set_operations(set_x, set_y):
    """
    Calculates the intersection and union of two sets (represented as lists)
    and returns their size difference (intersection_size - union_size).
    
    Args:
        set_x (list or set): First input collection.
        set_y (list or set): Second input collection.
        
    Returns:
        float: The difference between the size of intersection and size of union.
               Note: Intersection is always <= Union, so this value will be negative 
               or zero unless handled as absolute difference per specific interpretation.
               Standard math definition: |Intersection| - |Union|.
    """
    # Convert inputs to sets if they are lists/tuples for efficient operations
    s_x = set(set_x)
    s_y = set(set_y)

    intersection_size = len(s_x & s_y)
    union_size = len(s_x | s_y)

    difference = intersection_size - union_size
    
    return float(difference)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, files, or network)
    set_a = [10, 20, 30, 40]
    set_b = [30, 40, 50, 60]

    result_diff = calculate_set_operations(set_a, set_b)

    # Optional: Print results for verification in the console without external input
    print("Intersection size:", len({10, 20, 30, 40} & {30, 40, 50, 60}))
    print("Union size:", len({10, 20, 30, 40} | {30, 40, 50, 60}))
    print(f"Size difference (Intersection - Union): {result_diff}")