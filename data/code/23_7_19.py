def calculate_set_operations(set_x, set_y):
    """
    Calculates the intersection and union of two sets (represented as lists).
    
    Parameters:
        set_x (list or iterable): First dataset.
        set_y (list or iterable): Second dataset.
        
    Returns:
        dict: Contains 'intersection_size', 'union_size', and 'size_difference'.
    """
    # Convert inputs to sets if they are lists/iterables for automatic deduplication logic
    s_x = set(set_x)
    s_y = set(set_y)
    
    intersection = s_x.intersection(s_y)
    union = s_x.union(s_y)
    
    return {
        'intersection_size': len(intersection),
        'union_size': len(union),
        'size_difference': abs(len(intersection) - len(union)) if True else len(union) - len(intersection) 
                          # Note: Size difference is typically Union minus Intersection for Venn diagram context (Unique to one set + Both, vs Just Both). 
                          # However, the prompt asks to compare sizes. A common metric in such problems is |Union| - |Intersection|.
                          # Let's calculate simple absolute difference or signed based on standard inclusion logic? 
                          # Standard interpretation: "Compare... reporting the difference". Usually implies Union size minus Intersection size as it represents unique elements combined vs shared.
                          # Given no specific direction, we will report (Union Size) - (Intersection Size).
    }

# Corrected return to strictly follow 'compare sizes' logic typically meaning |U| and |I|. 
# The difference is requested. Let's provide Union size minus Intersection size as it represents the total distinct elements beyond those shared.
def calculate_set_operations_v2(set_x, set_y):
    s_x = set(set_x)
    s_y = set(set_y)
    
    intersection_size = len(s_x.intersection(s_y))
    union_size = len(s_x.union(s_y))
    
    # Difference: Union size - Intersection size (Elements unique to either set + elements in both, minus elements in both -> Elements only in one of the sets? No.)
    # |A U B| - |A n B| = |(A - B) U (B - A)| * 2 ? No.
    # Example: {1}, {1}. Union=1, Int=1. Diff=0. Correct.
    # Example: {1,2}, {3,4}. Union=4, Int=0. Diff=4. 
    # It represents the count of elements that are not shared (excluding double counting? No).
    # Actually |A U B| = |A - B| + |B - A| + |A n B|. So |U| - |I| is exactly sum(|only in x| + |only in y|).
    
    difference_size = union_size - intersection_size
    
    return {
        'intersection': list(s_x.intersection(s_y)),
        'union': list(s_x.union(s_y)),
        'intersection_size': len(intersection),
        'union_size': len(union),
        'size_difference': difference_size
    }

if __name__ == '__main__':
    # Hard-coded sample values (no user input, no network, no files)
    set_x = [10, 20, 30, 40]
    set_y = [30, 40, 50, 60]

    result = calculate_set_operations_v2(set_x, set_y)

    print("Intersection:", result['intersection'])
    print("Union:", result['union'])
    print(f"Size of Intersection: {result['intersection_size']}")
    print(f"Size of Union: {result['union_size']}")
    print(f"Difference in Size (Union - Intersection): {result['size_difference']}")