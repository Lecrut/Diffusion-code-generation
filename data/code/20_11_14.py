import copy

class ItemComparer:
    """A class to perform deep equality checks between complex data structures."""

    def check_equality(self, a, b):
        """
        Performs a deep comparison of two objects (lists and dictionaries).
        
        Args:
            a: The first object.
            iterables or dicts are supported for recursion.
            
        Returns:
            bool: True if the structures contain identical elements at all levels, False otherwise.
        """
        # Handle basic types that should not be recursively compared as containers
        if isinstance(a, (str, int, float, bool)) and a is b or type(a) == type(b):
            return a == b
        
        # If both are lists or tuples of the same length with matching elements at each level
        elif isinstance(a, list) and isinstance(b, list):
            if len(a) != len(b):
                return False
            
            for item_a, item_b in zip(a, b):
                if not self.check_equality(item_a, item_b):
                    return False
            return True
        
        # If both are dictionaries with the same keys and matching values at each level
        elif isinstance(a, dict) and isinstance(b, dict):
            if set(a.keys()) != set(b.keys()):
                return False
            
            for key in a:
                value_a = a[key]
                value_b = b.get(key)  # Use .get() to handle missing keys gracefully
                
                # If one exists but the other doesn't, they are not equal
                if value_a is None and value_b is None:
                    continue
                    
                elif isinstance(value_a, (list, dict)) or isinstance(value_b, (list, dict)):
                    if not self.check_equality(value_a, value_b):
                        return False
                        
                else:
                    # For non-container types, direct comparison should suffice. 
                    # However, to ensure robustness against mutable objects that aren't lists/dicts,
                    # we can use identity check for primitives or deep copy if needed.
                    # Given the prompt specifies "nested lists and dictionaries", simple equality is usually sufficient here.
                    # But let's be extra safe with non-container types by ensuring they are value-equal.
                    if not (value_a == value_b):
                        return False
                        
            return True
        
        else:
            # If one is a container type but the other isn't, or both aren't matching types for containers
            return False

if __name__ == '__main__':
    comparer = ItemComparer()

    sample_list_a = [1, 2, {'x': 'a', 'y': ['b', 'c']}]
    sample_list_b = [1, 2, {'x': 'a', 'y': ['b', 'c']}]
    
    sample_dict_a = {"name": "Alice", "scores": [90, 85], "tags": ["python"]}
    sample_dict_b = {"name": "Bob", "scores": [90, 85], "tags": ["java"]}

    print(f"List Equality: {comparer.check_equality(sample_list_a, sample_list_b)}") # Expected: True
    print(f"Dict Equality (Alice vs Bob): {comparer.check_equality(sample_dict_a, sample_dict_b)}") # Expected: False
    
    # Test with nested lists inside dicts
    complex_obj_1 = {"data": [[1, 2], [3, {'nested': 'deep'}]]}
    complex_obj_2 = {"data": [[1, 2], [3, {'nested': 'deep'}]]}
    
    print(f"Complex Nested Equality: {comparer.check_equality(complex_obj_1, complex_obj_2)}") # Expected: True
    
    # Test with mismatched types in structure (list vs dict)
    mixed_a = {"key": "value"}
    mixed_b = ["key", "value"]
    
    print(f"Mismatch Type Equality: {comparer.check_equality(mixed_a, mixed_b)}") # Expected: False
    
    # Test with missing keys in one dictionary (should return false based on logic above)
    dict_missing_key_1 = {"a": 1}
    dict_missing_key_2 = {"b": 1}
    
    print(f"Missing Keys Equality: {comparer.check_equality(dict_missing_key_1, dict_missing_key_2)}") # Expected: False
    
    # Test with None values in nested structures
    none_test_a = [None]
    none_test_b = [None]
    
    print(f"None Value Equality: {comparer.check_equality(none_test_a, none_test_b)}") # Expected: True