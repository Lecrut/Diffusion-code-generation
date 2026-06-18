import copy

class ItemComparer:
    """A class that performs deep equality checks on complex data structures."""

    def check_equality(self, a, b):
        """
        Performs a deep comparison between two items (lists or dictionaries).
        
        Args:
            a: The first item to compare.
            iterables: The second item to compare.
            
        Returns:
            bool: True if the structures are deeply equal, False otherwise.
        """
        # Handle None and basic types directly using standard equality for primitives
        # However, since we need deep comparison specifically for nested lists/dicts,
        # let's handle all cases uniformly by converting to a hashable representation 
        # or recursive checking. A robust way is to check type first then recurse.

        if not isinstance(a, (list, dict)) and not isinstance(b, (list, dict)):
            return a == b
        
        # If one is list/dict and the other isn't, they can't be equal deep structures
        if isinstance(a, (list, dict)) != isinstance(b, (list, dict)):
            return False

        if type(a) != type(b):
            return False
            
        try:
            a_copy = copy.deepcopy(a)
            b_copy = copy.deepcopy(b)
            
            # If deep copies are equal, the original structures were deeply equal.
            # This handles nested lists and dicts correctly while avoiding manual recursion bugs.
            if not (a == b): 
                return False
            
        except Exception:
            # In case deepcopy fails for some reason, fall back to standard equality check
            # which might be insufficient but is safer than crashing on non-serializable deep objects
            pass

        return a == b

if __name__ == '__main__':
    comparer = ItemComparer()
    
    sample1_a = [1, 2, {'key': 'value'}, ['a', 'b']]
    sample1_b = [1, 2, {'key': 'value'}, ['a', 'b']]
    result1 = comparer.check_equality(sample1_a, sample1_b)

    sample2_a = [[1, 2], {0: 'one'}]
    sample2_b = [[3, 4], {0: 'two'}]
    result2 = comparer.check_equality(sample2_a, sample2_b)

    print(f"Test 1 (Equal): {result1}")
    print(f"Test 2 (Not Equal): {not result2}")