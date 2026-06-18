def calculate_set_operations(set_x, set_y):
    """
    Calculates the intersection and union of two sets (or list-like inputs treated as sets).
    
    Args:
        set_x: First collection of data elements.
        set_y: Second collection of data elements.
        
    Returns:
        A dictionary containing 'intersection', 'union', and 'size_difference'.
    """
    # Convert input lists to actual sets for efficient operations
    s1 = set(set_x)
    s2 = set(set_y)
    
    intersection_result = list(s1 & s2)
    union_result = list(s1 | s2)
    
    size_intersection = len(intersection_result)
    size_union = len(union_result)
    
    # Calculate the difference in size (Union - Intersection is typically non-negative for sets, 
    # but we report simple subtraction as requested: Intersection Size - Union Size or vice versa?
    # The prompt asks to "compare... reporting the difference". Usually |A U B| >= |A n B|.
    # We will compute Difference = Size of Union - Size of Intersection.
    size_difference = size_union - size_intersection
    
    return {
        'intersection': intersection_result,
        'union': union_result,
        'size_of_intersection': size_intersection,
        'size_of_union': size_union,
        'difference_in_size': size_difference
    }

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    set_x = [10, 20, 30, 40]
    set_y = [30, 40, 50, 60]

    result = calculate_set_operations(set_x, set_y)

    print("Intersection:", result['intersection'])
    print("Union:", result['union'])
    print(f"Size of Intersection: {result['size_of_intersection']}")
    print(f"Size of Union: {result['size_of_union']}")
    print(f"Difference in Size (Union - Intersection): {result['difference_in_size']}")