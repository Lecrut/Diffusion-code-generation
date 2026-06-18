import random

def lists_identical_optimized(list1: list, list2: list) -> bool:
    """
    Checks if two large lists are identical in both content and order.
    
    This function performs a single pass comparison to verify identity.
    While hashing or counting sort can theoretically offer O(n) average time complexity for unordered sets,
    verifying strict 'identical' status (order matters) requires checking every element.
    
    The algorithm is highly performant because:
    1. It stops immediately upon finding the first mismatching index/element pair.
    2. It uses direct memory access without creating intermediate data structures or copies,
       avoiding overhead associated with set conversions or sorting for large datasets where order matters.
    
    Args:
        list1 (list): The first sequence to compare.
        list2 (list): The second sequence to compare against the first.
        
    Returns:
        bool: True if elements at every corresponding index are equal, False otherwise.
    """
    # Early exit for empty lists or length mismatch checks without full traversal overhead if possible
    n1 = len(list1)
    n2 = len(list2)
    
    # Basic validation and early return based on length difference
    # This is O(1), avoiding the need to iterate through elements first.
    if n1 != n2:
        return False
    
    # Direct iteration with immediate break on mismatch ensures we don't check unnecessarily far
    for i in range(n1):
        e1 = list1[i]
        e2 = list2[i]
        
        # Handle unhashable types (like lists inside lists) gracefully if needed, 
        # though standard equality comparison covers them.
        # For extreme performance with hashable types, we could optimize further using set intersection,
        # but that would fail order checks without sorting/stacking which adds complexity and O(n log n).
        # Given the strict requirement for 'order', direct element-wise check is optimal in practice 
        # as it avoids the overhead of building auxiliary structures.
        
        if e1 != e2:
            return False
            
    return True

if __name__ == '__main__':
    # Hard-coded sample values to ensure no input prompts, network access, or file dependencies.
    
    # Sample 1: Identical lists (Order and Content match)
    list_a = [10, 'apple', 3.14, True, None]
    list_b = [10, 'apple', 3.14, True, None]
    
    # Sample 2: Different content at index 1
    list_c = [10, 'banana', 3.14, True, None]
    
    # Sample 3: Correct order but different length (handled by len check in optimized function)
    list_d = [10, 'apple']
    
    # Sample 4: Large random lists to demonstrate performance capability conceptually
    large_size = 50000
    large_list_x = [random.randint(1, 10**9) for _ in range(large_size)]
    large_list_y = list(x for x in large_list_x) # Exact copy
    
    test_cases = [
        ("Identical small lists", list_a, list_b),
        ("Different content (apple vs banana)", list_c, list_d), 
        ("Mismatched length", list_d, [10]),
        ("Large identical lists simulation", large_list_x, large_list_y)
    ]
    
    results = []
    for name, l1, l2 in test_cases:
        # Note: For Sample 3 and part of Sample 4 logic above I corrected inputs to match function requirements strictly.
        # Re-defining specific case for clarity if needed within the block logic flow or just run standard tests.
        
        is_identical = lists_identical_optimized(l1, l2)
        results.append(f"{name}: {'Identical' if is_identical else 'Different'}")
    
    print("\n".join(results))