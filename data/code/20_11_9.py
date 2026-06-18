import copy

class ItemComparer:
    """A class that performs deep equality checks on complex data structures."""

    def check_equality(self, a, b):
        """
        Performs a deep comparison between two objects (lists and dictionaries).
        
        Args:
            a: The first object to compare.
            b: The second object to compare.
            
        Returns:
            bool: True if the structures are deeply equal, False otherwise.
        """
        # Handle basic types that should not be recursively checked for equality in this context
        # unless they are lists or dicts as per requirements. We treat primitives directly.
        
        # Check type first to handle non-list/dict cases gracefully based on requirement focus
        if isinstance(a, (list, dict)) and isinstance(b, (list, dict)):
            return self._deep_compare_recursive(a, b)
        else:
            # For any other types or mismatched list/dict types, use standard equality 
            # but ensure structural integrity is respected for the specific task of nested structures.
            # If one is a list and the other isn't, they are not equal.
            return type(a).__name__ == type(b).__name__ and (a == b)

    def _deep_compare_recursive(self, obj1, obj2):
        """Helper method to recursively compare lists and dictionaries."""
        
        # If types don't match at this level of recursion (e.g., list vs dict), return False
        if type(obj1) != type(obj2):
            return False
        
        try:
            length = len(obj1)
            
            # Check lengths for sequences
            if isinstance(obj1, (list, tuple)):
                if len(obj1) != len(obj2):
                    return False
                
                # Iterate through each element in the list/tuple
                for i in range(len(obj1)):
                    if not self._deep_compare_recursive(obj1[i], obj2[i]):
                        return False
                        
            elif isinstance(obj1, dict):
                # Check keys and values for dictionaries
                if set(obj1.keys()) != set(obj2.keys()):
                    return False
                
                for key in obj1:
                    if key not in obj2 or not self._deep_compare_recursive(
                        obj1[key], 
                        obj2[key]
                    ):
                        return False
                        
            else:
                # For other types, use standard equality check (assuming they are immutable primitives)
                return obj1 == obj2
                
        except Exception:
            # In case of any unexpected error during comparison, treat as not equal to be safe.
            return False

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    comparer = ItemComparer()

    # Test Case 1: Simple lists and dicts with nested structures
    test_data_1_a = [1, {"key": "value"}, ["nested", True]]
    test_data_1_b = [1, {"key": "value"}, ["nested", True]]
    
    result_1 = comparer.check_equality(test_data_1_a, test_data_1_b)

    # Test Case 2: Different nested structures (should return False)
    test_data_2_a = [{"a": 1}, [1, 2]]
    test_data_2_b = [{"b": 2}, [3, 4]]
    
    result_2 = comparer.check_equality(test_data_2_a, test_data_2_b)

    # Test Case 3: Non-list/dict types (should return True if equal values)
    test_data_3_a = "string"
    test_data_3_b = "string"
    
    result_3 = comparer.check_equality(test_data_3_a, test_data_3_b)

    # Test Case 4: Mixed type mismatch in structure (list vs string)
    test_data_4_a = [1]
    test_data_4_b = "1"
    
    result_4 = comparer.check_equality(test_data_4_a, test_data_4_b)

    print(f"Test Case 1 (Equal nested): {result_1}") # Expected: True
    print(f"Test Case 2 (Unequal nested): {result_2}") # Expected: False
    print(f"Test Case 3 (Simple strings): {result_3}") # Expected: True
    print(f"Test Case 4 (Type mismatch): {result_4}") # Expected: False
    
    assert result_1 == True, "Test Case 1 failed."
    assert result_2 == False, "Test Case 2 failed."
    assert result_3 == True, "Test Case 3 failed."
    assert result_4 == False, "Test Case 4 failed."

    print("All tests passed successfully.")