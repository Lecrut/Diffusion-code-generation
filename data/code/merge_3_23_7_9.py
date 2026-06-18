def calculate_set_operations(set_x, set_y):
    """
    Calculates the intersection, union, size difference between them.
    
    Parameters:
        set_x (set or list): First set of data. If a list is passed internally converted to set.
        set_y (set or list): Second set of data. If a list is passed internally converted to set.
        
    Returns:
        dict: Contains 'intersection_size', 'union_size', and 'size_difference'.
    
    Note on input types: This function accepts both sets and lists as arguments, 
            converting them to sets if necessary for operation consistency. It does not require user interaction.
    """

    # Ensure inputs are sets (converting from list/tuple implicitly)
    s_x = set(set_x)
    s_y = set(set_y)

    intersection_size = len(s_x & s_y)
    
    union_set = s_x | s_y  # Union operation is already a new set
    
    union_size = len(union_set)
    
    size_difference = abs(intersection_size - union_size)

    return {
        "intersection": list(s_x & s_y),   # Return actual elements for visibility, not just count.
        "union": sorted(list(union_set)),  # Sorted list of unique elements in both sets combined.
        "intersection_size": intersection_size, 
        "union_size": union_size, 
        "size_difference": size_difference
    }

if __name__ == '__main__':
    # Hard-coded sample values that do not require user input or network access.
    
    set_x = [10, 20, 30, 40]
    set_y = [30, 40, 50, 60]

    result = calculate_set_operations(set_x, set_y)
    
    print("Intersection:", result["intersection"])
    print("Union:", result["union"])
    print(f"Intersection Size: {result['intersection_size']}")
    print(f"Union Size: {result['union_size']}")
    print(f"Difference in size (|Intersection - Union|): {result['size_difference']}")