import numpy as np

class VectorComparator:
    """A class to perform element-wise comparisons on numeric vectors."""

    @staticmethod
    def is_less_than_or_equal_first_diff(vec1, vec2):
        """
        Compares two lists of numbers element-wise.
        
        Returns True if the first vector's value at the index 
        where they differ (if any) is less than or equal to the second vector's value.
        If all elements are identical, returns False as there is no differing element 
        for comparison logic defined by 'first differing'. However, per standard interpretation 
        of such problems where equality implies condition met up to that point but strictly 
        requires a difference: if vec1 == vec2, we return False because the set of first-differing elements is empty.
        
        If no differences exist (vectors are identical), this method returns False based on strict logic 
        requiring a differing element context. Alternatively, some interpretations treat equality as satisfying <= everywhere.
        Given the specific constraint "considering only the first differing element", if none exists:
        - We cannot identify such an element -> Return False to indicate condition not met via difference check.

        Args:
            vec1 (list): First list of numbers.
            vec2 (list): Second list of numbers.

        Returns:
            bool: True if at the first index where elements differ, vec1[i] <= vec2[i]. 
                  If vectors are identical, returns False as no differing element exists to satisfy the condition strictly.
        """
        
        # Handle empty lists or single-element cases explicitly for clarity
        if not isinstance(vec1, list) or not isinstance(vec2, list):
            raise TypeError("Both arguments must be lists.")

        min_len = min(len(vec1), len(vec2))
        
        # Iterate up to the length of the shorter vector
        for i in range(min_len):
            val1 = vec1[i]
            val2 = vec2[i]
            
            if val1 != val2:
                # Found first differing element; check condition
                return val1 <= val2
        
        # If loop completes without returning, vectors are identical up to min length.
        # Since no "first differing" element exists within the common range (and we assume 
        # comparison stops at shorter list or requires difference), we default to False.
        return False

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    test_cases = [
        ([1, 2, 3], [4, 5, 6]),           # First diff at index 0: 1 <= 4 -> True
        ([5, 2, 3], [1, 5, 6]),           # First diff at index 0: 5 > 1 -> False
        ([1, 1, 1], [1, 2, 3]),           # First diff at index 1: 1 <= 2 -> True
        ([4, 4, 4], [4, 4, 4]),            # Identical vectors -> No first difference -> False (per logic)
        ([0.5, 2.7], [3.9, 8.1]),          # First diff at index 0: 0.5 <= 3.9 -> True
    ]

    results = []
    
    for i, (v1, v2) in enumerate(test_cases):
        res = VectorComparator.is_less_than_or_equal_first_diff(v1, v2)
        print(f"Test Case {i + 1}: vec1={v1}, vec2={v2} -> Result: {res}")
        
    # Additional manual verification output for clarity if needed in future expansions