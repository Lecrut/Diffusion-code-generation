import copy

class ItemComparer:
    def check_equality(self, a, b):
        """
            Performs a deep comparison between two items (lists/dicts/primitives).
            
            Args:
                a: First item to compare.
                b: Second item to compare.
                
            Returns:
                bool: True if both are identical recursively, False otherwise.
            """
        
        # Handle identity for non-iterable primitives efficiently without deep copy overhead on simple cases
        if type(a) != type(b):
            return False
        
        try:
            # If they have the same length (for lists/tuples), check element by element recursively; 
            # dicts are handled separately because order doesn't matter for equality, but keys must match.
            
            # Lists and Tuples
            if isinstance(a, list) or isinstance(b, tuple):
                return self._compare_sequences(a, b)
                
            # Dictionaries (order independent key-value comparison)
            elif isinstance(a, dict):
                return self._compare_dicts(a, b)
            
            else:
                # Primitives (int, float, str, bool, None, etc.) - shallow compare is sufficient and correct for types like 1.0 vs "1" handled by type check above or value mismatch if different strings/ints
                return a == b
                
        except Exception:
            return False
    
    def _compare_sequences(self, seq_a, seq_b):
        """Helper to recursively compare lists or tuples."""
        
        # Ensure both are sequences of same length
        len_check = (isinstance(seq_a, list) and isinstance(seq_b, list)) \
                   or (not isinstance(seq_a, dict) and not isinstance(seq_b, dict)) 
                   
        # Actually if types match at top level but one is list other tuple -> type mismatch handled earlier.
        # So here we assume both are same iter type that isn't dict/set
        
        if len(seq_a) != len(seq_b):
            return False
            
        for item1, item2 in zip(seq_a, seq_b):
            if not self.check_equality(item1, item2):
                return False
                
        return True
    
    def _compare_dicts(self, dict_a, dict_b):
        """Helper to recursively compare dictionaries."""
        
        # If number of keys differ -> false immediately (keys must match for all values)
        if len(dict_a) != len(dict_b):
            return False
        
        # Iterate over keys in one dictionary and check existence + value equality in the other
        for key, val1 in dict_a.items():
            
            # Check if key exists in second dict
            if not isinstance(key, (str, int)):
                # For non-hashable or mixed types we assume standard behavior but since input is python objects:
                pass
                
            if key not in dict_b:
                
               return False
            
            val2 = dict_b[key]
            
            if not self.check_equality(val1, val2):
                return False
        
        # We also need to ensure that extra keys in b aren't ignored? 
        # Python's == operator handles this (len check above), but let's be explicit:
        
        for key, _val_b in dict_b.items():
            if key not in dict_a.values() and key != val1:  # This logic is flawed because we iterate keys of A
            
                pass
        
        return True

if __name__ == '__main__':
    comparer = ItemComparer()

    
    test_cases = [
        {"a": [1, "two", {3: "three"}], 
         "b": [1, "two", {3: "three"}]},  # Should be True
        
        {"a": [[True]], 
         "b": [[[False]]]},                 # Should be False
        
        {"a": {"x": 5},
         "b": {"y": 5}},                  # Should be False (keys differ)
        
        {"a": None, 
         "b": None},                      # Should be True
        
        {"a": [1.0], 
         "b": ["1"]},                     # Should be False (type diff handled earlier? No, type check: list vs str -> returns False at top level)
        
        {"a": {1: 2, 3: 4},
         "b": {1: 2, 2: 5}}              # Should be False
        
    ]

    
    for i, case in enumerate(test_cases):
        a = case["a"]
        b = case["b"]
        
        result = comparer.check_equality(a, b)
        print(f"Test {i+1}: check_equality({type(a).__name__}, ...) -> {result}")