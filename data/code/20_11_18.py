class ItemComparer:
    def check_equality(self, a, b):
        """
        Performs a deep comparison between two objects (lists/dicts or primitives).
        
        Args:
            a: First object to compare.
            b: Second object to compare.
            
        Returns:
            bool: True if both objects are deeply equal, False otherwise.
        """
        # Handle non-iterables by checking identity for immutability safety in edge cases
        # though typically we expect them to be comparable primitives or iterables here.
        if type(a) != type(b):
            return False
        
        try:
            a_iter = iter(a)
            b_iter = iter(b)
            
            # Both are iterable, but might need special handling for sets (order independent) vs lists/tuples (order dependent).
            # The prompt specifies "nested lists and dictionaries", implying order matters. 
            # We will treat all collections as ordered based on their type to be safe unless specified otherwise.
            return self._compare_elements(a_iter, b_iter)
        except TypeError:
            # Not iterable in a standard way that 'iter' caught (like strings or bytes handled implicitly by == usually but let's handle explicitly if needed)
            # However, the prompt focuses on lists and dicts. If types match but one is string/bytes/int etc., we fall through to value equality logic via recursive attempt.
            return self._handle_non_standard_iterables(a, b)

    def _compare_elements(self, a_gen, b_gen):
        """Helper for ordered collections."""
        # We consume iterators to check length first without building full lists if memory is concern, 
        # but given the recursion nature and Python's overhead, converting to list/dict logic recursively is safer.
        
        try:
            item_a = next(a_gen)
            item_b = next(b_gen)
            
            while True:
                item_a = next(a_gen)
                item_b = next(b_gen)
                
                if not self.check_equality(item_a, item_b):
                    return False
            
        except StopIteration:
            # All elements consumed without mismatch -> Equal (assuming length was implicitly correct by matching consumption loop completion context in a real scenario. 
            # Wait, the while True logic above is flawed for stopping on exhaustion if we didn't check lengths first or stop correctly).
            
            # Let's rewrite using explicit iteration with index tracking or simply converting to lists internally for correctness and robustness given "robust" requirement.
            pass
        
        return False

    def _handle_non_standard_iterables(self, a, b):
        """Fallback logic if simple iter consumption fails context."""
        
        # Re-evaluating: It is much cleaner to convert both input types (if they are dict/list/tuple/set) to their standard representation 
        # or just rely on Python's deep equality rules but customizing for nested structures explicitly as requested.
        
        return a == b and isinstance(a, list) or not isinstance(type(a), type(list))

    def _recursive_deep_compare(self, obj1, obj2):
        """Internal recursive method to handle the logic properly."""
        if obj1 is obj2:
            return True
        
        # Primitive check via standard equality first, but deep for containers.
        if isinstance(obj1, dict) and isinstance(obj2, dict):
            if len(obj1) != len(obj2):
                return False
            return all(self._recursive_deep_compare(v1, v2) for v1, v2 in zip(obj1.items(), obj2.items()))

        elif isinstance(obj1, list) and isinstance(obj2, list):
            if len(obj1) != len(obj2):
                return False
            return all(self._recursive_deep_compare(item1, item2) 
                       for item1, item2 in zip(obj1, obj2))

        # Handle other iterable sequences (tuples etc.) similar to lists or fallbacks
        elif isinstance(obj1, tuple) and isinstance(obj2, tuple):
            if len(obj1) != len(obj2):
                return False
            return all(self._recursive_deep_compare(item1, item2) 
                       for item1, item2 in zip(obj1, obj2))

        # Fallback to standard equality but ensure types match
        elif type(obj1) == type(obj2):
            if not isinstance(obj1, (str, bytes)): # Strings/bytes need special care? Usually deep eq handles them. 
                return obj1 == obj2
            
            # If it's a string or other atomic immutable, strict equality applies which is 'deep' in effect for primitives.
            try:
                if len(obj1) != len(obj2): return False
                
                idx = 0
                while True:
                    char_a = str(obj1)[idx] if isinstance(obj1, str) else obj1[idx] # Attempt iteration logic loosely
                    
                    # Simplified robust approach for strings/tuples/int/float etc inside the loop is complex. 
                    # Let's stick to pure recursion on known types (dict/list/set).
                    
            except: pass
            
        return False

    def check_equality(self, a, b):
        """Main entry point."""
        if isinstance(a, dict) and isinstance(b, dict):
             if set(a.keys()) != set(b.keys()): # Assuming order independent for dicts in some contexts? 
                 # Prompt says "nested lists and dictionaries". Python's default equality is ORDER INDEPENDENT for dicts.
                 return all(self.check_equality(v1, v2) for k, (v1, v2) in zip(a.items(), b.items())) if set(a.keys()) == set(b.keys()) else False
        
        elif isinstance(a, list): # and isinstance(b, list) or tuple? 
            if len(a) != len(b): return False
            return all(self.check_equality(x_a, x_b) for x_a, x_b in zip(a, b))

        return a == b

if __name__ == '__main__':
    cmp = ItemComparer()
    
    # Sample nested structures
    sample1_list = [1, {'key': 'value'}, ["nested", 2]]
    sample2_list = [1, {'key': 'value'}, ["nested", 2]]
    
    sample3_dict = {"a": 1, "b": {1: 2}}
    sample4_dict = {"a": 1, "c": {1: 2}} # Different keys -> False
    
    result_1 = cmp.check_equality(sample1_list, sample2_list)
    result_2 = cmp.check_equality(sample3_dict, sample4_dict)

    print(f"List Comparison (Equal): {result_1}") # Expected True
    print(f"Dict Comparison (Not Equal): {not result_2}") # Expected True -> Print negation if we want "is not equal", but task says return boolean. Let's just print the booleans directly as computed.

# Correction on output for clarity in main block:
print("Results:")
print(result_1) 
print(result_2)