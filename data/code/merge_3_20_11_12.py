import copy

class ItemComparer:
    """A class that performs deep equality checks between nested structures."""

    def check_equality(self, a, b):
        """
        Performs a deep comparison of two objects (lists and dictionaries).
        
        Args:
            a: The first object to compare.
            iterables: The second object to compare.
            
        Returns:
            bool: True if the structures are deeply equal, False otherwise.
        """
        # If both are None or single values of same type and equal
        if isinstance(a, dict) and isinstance(b, dict):
            return self._compare_dicts(a, b)
        
        elif isinstance(a, list) and isinstance(b, list):
            return self._compare_lists(a, b)
            
        else:
            # For non-dict/list types (e.g., int, str), check standard equality
            return a == b

    def _compare_dicts(self, dict_a, dict_b):
        """Helper method to recursively compare two dictionaries."""
        if len(dict_a) != len(dict_b):
            return False
        
        for key in dict_a:
            if key not in dict_b or self.check_equality(dict_a[key], dict_b[key]) is False:
                return False
                
        return True

    def _compare_lists(self, list_a, list_b):
        """Helper method to recursively compare two lists."""
        len_a = len(list_a)
        len_b = len(list_b)
        
        if len_a != len_b:
            return False
        
        for i in range(len_a):
            if self.check_equality(list_a[i], list_b[i]) is False:
                return False
                
        return True

if __name__ == '__main__':
    # Hard-coded sample values to test the class without user input
    
    comparer = ItemComparer()
    
    # Test Case 1: Simple integers and strings (should be equal)
    simple_a = {"name": "Alice", "age": 30}
    simple_b = {"name": "Alice", "age": 30}
    result_1 = comparer.check_equality(simple_a, simple_b)
    
    # Test Case 2: Nested lists (should be equal)
    nested_list_a = [1, [2, 3], [4]]
    nested_list_b = [1, [2, 3], [4]]
    result_2 = comparer.check_equality(nested_list_a, nested_list_b)
    
    # Test Case 3: Nested lists with different content (should be unequal)
    nested_list_diff_a = [1, [2, 3], [5]]
    nested_list_diff_b = [1, [2, 3], [4]]
    result_3 = comparer.check_equality(nested_list_diff_a, nested_list_diff_b)
    
    # Test Case 4: Mixed structure (dict containing list) (should be equal)
    mixed_a = {"items": [[1, 2], {0: "zero"}]}
    mixed_b = {"items": [[1, 2], {0: "zero"}]}
    result_4 = comparer.check_equality(mixed_a, mixed_b)
    
    # Test Case 5: Mixed structure with difference (should be unequal)
    mixed_diff_a = {"items": [[1, 2], {0: "one"}]}
    mixed_diff_b = {"items": [[1, 2], {0: "zero"}]}
    result_5 = comparer.check_equality(mixed_diff_a, mixed_diff_b)
    
    # Test Case 6: None vs empty list (should be unequal)
    none_val = None
    empty_list = []
    result_6 = comparer.check_equality(none_val, empty_list)

    print(f"Test 1 (Simple Dicts Equal): {result_1}")      # Expected True
    print(f"Test 2 (Nested Lists Equal): {result_2}")   # Expected True
    print(f"Test 3 (Nested Lists Unequal): {result_3}")# Expected False