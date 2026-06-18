import copy

class ItemComparer:
    def check_equality(self, a, b):
        """
        Performs a deep comparison between two objects (lists or dictionaries).
        
        Args:
            a: The first object to compare.
            b: The second object to compare.
            
        Returns:
            bool: True if both objects are deeply equal, False otherwise.
        """
        # Handle basic type mismatch immediately
        if not isinstance(a, (list, dict)) or not isinstance(b, (list, dict)):
            return a == b
        
        # If types differ but one is list/dict and other isn't, they can't be equal deep-wise in this context
        # unless we consider non-container equality which the initial check handles. 
        # However, strict deep comparison for containers requires both to be same type of container.
        
        if not isinstance(a, (list, dict)) or not isinstance(b, (list, dict)):
            return a == b

        if type(a) != type(b):
            return False
        
        try:
            # For lists and dicts, we need deep equality check
            # Using copy.deepcopy to ensure structural comparison of nested elements
            # Note: Standard '==' works for shallow structures but fails on deeply nested mutable objects.
            # We implement a recursive logic or use deepcopy + == which is robust enough 
            # provided the hashability isn't an issue (though deep equality doesn't require hashes).
            
            if isinstance(a, list):
                return self._deep_list_compare(a, b)
            elif isinstance(a, dict):
                return self._deep_dict_compare(a, b)
        except Exception:
            # If any internal error occurs during comparison structure traversal (e.g. unhashable in set logic if we used it), 
            # fall back to standard equality which might not be deep enough but handles basic cases safely.
            # However, for true robustness on nested lists/dicts without external libs:
            return False

    def _deep_list_compare(self, a, b):
        """Recursively compares two lists."""
        if len(a) != len(b):
            return False
        
        for i in range(len(a)):
            # Recurse into elements. If an element is not comparable (e.g., int vs str), standard equality handles it as false.
            # We assume all nested items are either primitives or containers that can be compared recursively.
            if a[i] != b[i]:
                return False
        
        return True

    def _deep_dict_compare(self, a, b):
        """Recursively compares two dictionaries."""
        if set(a.keys()) != set(b.keys()):
            return False
        
        for key in a:
            # If the values are not equal (which triggers deep comparison recursively) or keys don't match value-wise structure
            val_a = self.check_equality(a[key], b.get(key))
            if not val_a:
                return False
                
        return True

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input
    
    comparer = ItemComparer()

    # Test Case 1: Simple lists and dicts with nested structures
    item_1_list = [1, "hello", {"nested": [42, True]}]
    item_2_list = [1, "hello", {"nested": [42, True]}]
    
    result_test_1 = comparer.check_equality(item_1_list, item_2_list)

    # Test Case 2: Lists with different nested values
    item_3_list = [1, "world"]
    item_4_list = [1, "hello"]
    
    result_test_2 = comparer.check_equality(item_3_list, item_4_list)

    # Test Case 3: Dictionaries with deeply nested differences
    dict_a = {"x": 10, "y": {"z": list("abc")}}
    dict_b = {"x": 10, "y": {"z": list("abd")}}
    
    result_test_3 = comparer.check_equality(dict_a, dict_b)

    # Test Case 4: Mixed types that should not be equal deep-wise even if shallow look similar
    item_mixed = [1]
    item_other = (1,)
    
    result_test_4 = comparer.check_equality(item_mixed, item_other)

    print(f"Test 1 (Equal nested structures): {result_test_1}") # Expected: True
    print(f"Test 2 (Different strings in list): {result_test_2}") # Expected: False
    print(f"Test 3 (Different chars in dict value list): {result_test_3}") # Expected: False
    print(f"Test 4 (List vs Tuple): {result_test_4}") # Expected: False
    
    # Final verification block to ensure all tests ran without error
    assert result_test_1 == True, "Failed Test 1"
    assert result_test_2 == False, "Failed Test 2"
    assert result_test_3 == False, "Failed Test 3"
    assert result_test_4 == False, "Failed Test 4"

    print("All tests passed successfully.")