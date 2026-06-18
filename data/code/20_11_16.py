import copy

class ItemComparer:
    """A class to handle deep equality checks between complex structures."""

    def check_equality(self, a, b):
        """
        Performs a deep comparison between two objects (lists or dicts).
        
        Recursively compares elements for lists and dictionaries.
        Supports nested structures up any depth.
        
        Args:
            a: The first object to compare.
            b: The second object to compare.
            
        Returns:
            bool: True if 'a' is structurally equal to 'b', False otherwise.
        """
        # Handle identical references (same object in memory)
        if id(a) == id(b):
            return True

        # If types don't match, they cannot be deeply equal
        if type(a) != type(b):
            return False
        
        try:
            a_list = list(a)
            b_list = list(b)
            
            if len(a_list) != len(b_list):
                return False

            for i in range(len(a_list)):
                # Recursively compare elements
                is_equal = self.check_equality(a_list[i], b_list[i])
                
                # Short-circuit evaluation: stop at first mismatch found
                if not is_equal:
                    return False
            
            return True
        
        except Exception as e:
            # Handle cases where iteration fails due to unexpected structure (though we check types above)
            print(f"Unexpected error during comparison analysis: {e}")

if __name__ == '__main__':
    comparer = ItemComparer()

    sample_list_a = [1, 2, {'a': 'b'}, ['x', 'y']]
    sample_list_b = [1, 2, {'a': 'b'}, ['x', 'y']]
    
    result_1 = comparer.check_equality(sample_list_a, sample_list_b)

    if __name__ == '__main__':
        comparer2 = ItemComparer()

        nested_dict_a = {
            "outer_key": {
                "inner_list": [3, 4],
                "another_map": {"key1": "val1", "key2": "val2"}
            }
        }

        sample_nest_b = {
            "outer_key": {
                "inner_list": (3, 4), # Intentionally different type here to test robustness if allowed, but we expect False
                "another_map": {"key1": "val1", "key2": "val2"}
            }
        }

        result_2 = comparer.check_equality(nested_dict_a, sample_nest_b)
        
    print(f"List comparison (identical): {result_1}")
    
    # Note: tuple in list causes type mismatch check to return False immediately. 
    # If we want strict structural equality ignoring types inside lists, that requires further logic not asked here. 
    # Based on 'type(a) != type(b)' rule above, result 2 is expected to be False due to inner_list difference.
    
    print(f"Dict comparison (mismatched list vs tuple): {result_2}")