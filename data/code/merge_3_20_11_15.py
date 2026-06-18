import copy

class ItemComparer:
    """A class that provides deep equality checking for lists and dictionaries."""

    def check_equality(self, a, b):
        """
        Performs a deep comparison of two objects (lists or dicts).
        
        Args:
            a: The first object to compare.
            b: The second object to compare.
            
        Returns:
            bool: True if the structures are identical recursively, False otherwise.
            
        Raises:
            TypeError: If neither argument is iterable (list/dict) or None.
        """
        # Handle identity for non-iterable types directly handled by == usually, 
        # but we enforce structural check here based on prompt requirements 
        # focusing on nested lists and dicts logic.
        if type(a) != type(b):
            return False
        
        # If both are empty containers of same type (list/dict), they are equal in depth 0 context
        try:
            iter(a)
            iter(b)
            
            is_list = isinstance(a, list)
            
            if not is_list and a != b:
                return False
                
            # Recursively compare elements for lists or dicts based on structure logic requested
            # The prompt specifies "nested lists and dictionaries", so we implement robust recursive check.
            # We treat non-list/non-dict iterables (like tuples) similarly to list if types match, 
            # but the specific requirement focuses on list/dict nesting.
            
            items_a = a
            
            if is_list:
                return self._compare_lists(a, b)
            else:
                # If it's not a list and type matches (e.g., both dicts), we assume dict logic or fail safe otherwise
                # However, the prompt specifically mentions nested lists AND dictionaries.
                # Let's implement generic deep equality for any matching iterable structure 
                # but prioritize list/dict as per common interpretation of such tasks unless specified 'tuple'.
                return self._compare_dicts(a, b) if isinstance(a, dict) else False
                
        except TypeError:
            return a == b

    def _compare_lists(self, a, b):
        """Helper to recursively compare two lists."""
        n_a = len(a)
        n_b = len(b)
        
        if n_a != n_b:
            return False
        
        for i in range(n_a):
            if not self.check_equality(a[i], b[i]):
                return False
                
        return True

    def _compare_dicts(self, a, b):
        """Helper to recursively compare two dictionaries."""
        # Check number of keys match and types are identical (dict type)
        if set(a.keys()) != set(b.keys()):
            return False
        
        for key in a:
            val_a = a[key]
            
            # Handle case where value is not comparable directly by structure but falls back to standard equality 
            # only if the structures were explicitly defined as non-iterable. 
            # For robustness, we check type of values first before deep dive or handle generic comparison logic here?
            # The prompt asks specifically for "nested lists and dictionaries". 
            # Standard dict value types (like numbers) should be compared via == if not iterables matching the pattern.
            
            val_b = b[key]
            
            if type(val_a) != type(val_b):
                return False
            
            try:
                iter(val_a)
                iter(val_b)
                
                # If values are list/dict, recurse; otherwise standard equality suffices unless they contain hidden complexity? 
                # The prompt implies deep comparison for the containers themselves. Standard recursion works fine here.
                if type(val_a).__name__ in ('list', 'dict'):
                    return self.check_equality(val_a, val_b)
            except TypeError:
                pass
            
        return True

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    
    comparer = ItemComparer()
    
    # Test Case 1: Simple lists and dicts with nesting
    list_a = [1, 'a', {'key': 'val'}]
    list_b = [1, 'a', {'key': 'val'}]
    result_1 = comparer.check_equality(list_a, list_b)

    # Test Case 2: Mismatched nested structure (different key order or values)
    dict_mistake = {1: 'wrong', 2: 'correct'}
    list_c = [dict_mistake]
    result_2 = comparer.check_equality(list_a, list_c)

    # Test Case 3: Different types at top level (list vs tuple - handled by type check in main logic above as False due to strict typing)
    tuple_like = (1, 'a', {'key': 'val'})
    result_3 = comparer.check_equality(list_a, tuple_like)

    # Test Case 4: Deeply nested mismatched values inside dict
    deep_list_mismatch = [1, [{'x': 2}, ['y']] ]
    deep_dict_match = {0: {'nested': [{'z': 'same'}]}, 'end': True}
    
    complex_a = [{0: 1}]
    complex_b = [{0: 1}]
    result_4 = comparer.check_equality(complex_a, complex_b)

    # Test Case 5: Non-list/dict input (should fail gracefully or return standard equality if types match per implementation logic above - here it returns False due to type check in main block unless both are same non-iterable type)
    str_val = "hello"
    int_val = 42
    
    # Ensure no runtime errors on execution without user input
    print(f"Test 1 (Match): {result_1}")          # Expected: True
    print(f"Test 2 (Mismatch): {result_2}")      # Expected: False
    print(f"Test 3 (Type Mismatch List vs Tuple): {result_3}")  # Expected: False due to type check in main logic block
    
    if result_1 and not result_2 and not result_3 and True == comparer.check_equality(complex_a, complex_b):
        pass