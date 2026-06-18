import sys

def calculate_set_operations(set_x, set_y):
    """
    Calculates intersection and union of two sets (treated as lists/sets) 
    and returns their sizes along with the difference in size.
    
    Args:
        set_x (set or list): First dataset.
        set_y (set or list): Second dataset.
        
    Returns:
        dict: Contains 'intersection_size', 'union_size', and 'size_difference'.
              Size difference is defined as union_size - intersection_size.
    """
    # Convert inputs to sets if they aren't already for consistent handling
    s_x = set(set_x)
    s_y = set(set_y)

    # Calculate Intersection: elements present in both sets
    intersection = s_x.intersection(s_y)
    
    # Calculate Union: all unique elements from both sets
    union = s_x.union(s_y)

    size_difference = len(union) - len(intersection)

    return {
        'intersection_size': len(intersection),
        'union_size': len(union),
        'size_difference': size_difference,
        'intersection_elements': list(intersection),
        'union_elements': list(union)
    }

if __name__ == '__main__':
    # Hard-coded sample values ensuring no input() or file dependencies.
    set_x = {10, 20, 30, 40}
    set_y = {30, 40, 50, 60}

    result = calculate_set_operations(set_x, set_y)
    
    print("Intersection Elements:", result['intersection_elements'])
    print(f"Union Elements: {result['union_elements']}")
    print("\nOperation Results:")
    print(f"Size of Intersection: {result['intersection_size']}")
    print(f"Size of Union: {result['union_size']}")
    print(f"Difference in Size (Union - Intersection): {result['size_difference']}")