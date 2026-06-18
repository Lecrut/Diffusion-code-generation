import hashlib
from typing import List, Hashable

def check_identical_lists(list1: List[Hashable], list2: List[Hashable]) -> bool:
    """
    Checks if two lists are identical in both content and order.
    
    This implementation uses a step-by-step comparison to avoid unnecessary 
    full list traversals once a mismatch is found, ensuring high performance 
    for large datasets where early mismatches should terminate the check quickly.

    Args:
        list1 (List[Hashable]): The first list of hashable elements.
        list2 (List[Hashable]): The second list of hashable elements.

    Returns:
        bool: True if both lists are identical, False otherwise.
    
    Raises:
        TypeError: If input types or element types are not suitable for comparison.
    """
    # Handle different lengths immediately without iterating
    len1 = len(list1)
    len2 = len(list2)

    if len1 != len2:
        return False

    try:
        # Perform direct element-wise matching up to the point of mismatch or completion
        for i in range(len1):
            item1 = list1[i]
            item2 = list2[i]

            # Check type compatibility before value comparison to avoid deep hashing on complex objects unnecessarily
            if not isinstance(item1, type(item2)):
                return False
            
            try:
                if item1 != item2:
                    return False
            except TypeError:
                # If elements are uncomparable (e.g., mixed types in unexpected ways), fail fast
                raise

        return True
    except Exception as e:
        # Re-raise any internal errors for debugging clarity without wrapping user input logic
        raise

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without external inputs or files
    
    # Test Case 1: Identical lists
    list_a = [1, "apple", 3.14, True]
    list_b = [1, "apple", 3.14, True]
    assert check_identical_lists(list_a, list_b) == True

    # Test Case 2: Different lengths (mismatch at length level)
    list_c = [10, 20, 30]
    list_d = [10, 20]
    assert check_identical_lists(list_c, list_d) == False

    # Test Case 3: Same elements but different order (mismatch at index level)
    list_e = ["alpha", "beta"]
    list_f = ["beta", "alpha"]
    assert check_identical_lists(list_e, list_f) == False

    # Test Case 4: Mismatch in value type or content within same length
    list_g = [100]
    list_h = [200]
    assert check_identical_lists(list_g, list_h) == False

    # Test Case 5: Large list performance test (simulated with a loop to generate data)
    large_list_1 = []
    for i in range(10**4):
        large_list_1.append(i * 2 + 1)

    large_list_2 = large_list_1.copy() # Create an exact duplicate
    
    # Verify correctness on a larger scale without manual typing every element
    result_large = check_identical_lists(large_list_1, large_list_2)
    
    print(f"Test Case 5 (Large List): {'Passed' if result_large else 'Failed'}")

    # Demonstrate failure case for large lists with early mismatch
    large_list_mismatched = list(large_list_1[:]) 
    large_list_mismatched[len(large_list_1)//2] += 999
    
    result_mismatch = check_identical_lists(large_list_1, large_list_mismatched)
    print(f"Test Case Mismatch (Early Exit): {'Passed' if not result_mismatch else 'Failed'}")

    # Final assertion to ensure all logic holds together
    assert result_large == True and not result_mismatch
    
    print("All internal tests passed successfully.")