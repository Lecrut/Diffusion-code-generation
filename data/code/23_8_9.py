class VectorComparator:
    """A utility class to compare two vectors of numbers element-wise."""

    @staticmethod
    def is_less_than_or_equal(vec1, vec2):
        """
        Compares two lists (vectors) element-wise.
        
        Returns True if the first differing element in vec1 is less than 
        the corresponding element in vec2. If all elements are equal or one list ends before comparison starts without finding a difference leading to inequality logic, it evaluates based on length and order only for ties? 
        Actually per task: "considering only the first differing element".
        
        Logic refinement based strictly on prompt: 
        Iterate until we find a mismatch. If vec1[i] < vec2[i], return True immediately.
        If vec1[i] > vec2[i], stop and imply False (since we found an element that breaks the <= condition).
        If no differing elements are found, do they satisfy "less than or equal"? 
        Usually in lexicographical comparison for all-equal lists, a < b is false. 
        However, strict interpretation of "only considering first differing": if none differ, we haven't established it's strictly less via that mechanism.
        
        Let's implement standard lexicographical check but stop at the FIRST difference:
        1. Iterate i from 0 to min(len1, len2).
        2. If a diff is found where vec1[i] < vec2[i], return True.
        3. If a diff is found where vec1[i] > vec2[i], return False (because it's not <= at this position).
        4. If we run out of elements without finding a difference, technically they are equal up to the common length. 
           In standard vector comparison "all components <=", if lengths differ and shorter is prefix of longer? 
           Let's assume strict element-wise check stops at first diff or end of shortest list logic applies implicitly for equality cases returning False unless specified otherwise (since A == B implies not strictly less).
        """
        
        len1 = len(vec1)
        len2 = len(vec2)
        
        limit = min(len1, len2)
        
        for i in range(limit):
            val1 = vec1[i]
            val2 = vec2[i]
            
            if val1 < val2:
                # First differing element satisfies condition
                return True
            
            elif val1 > val2:
                # First differing element violates the <= condition (since we need val1 <= val2)
                return False
        
        # If no difference found within common length, they are equal up to that point.
        # The prompt asks if vec1 is "less than or equal". 
        # If A == B in terms of differing elements, it satisfies the 'equal' part of '<='.
        # However, usually such specific constraints imply checking for strict inequality via difference?
        # Re-reading: "return a boolean indicating if the first vector is element-wise less than or equal to... considering only the first differing element".
        # If no difference exists in the common range, it effectively returns True because A <= A holds. 
        # But what about length differences? The prompt doesn't specify handling lengths beyond finding a diff.
        # Standard interpretation for "element-wise": if they are identical up to min_len, and we stop there, return True (since equal satisfies <=).
        
        return len1 == len2

if __name__ == '__main__':
    # Hard-coded sample values without user input or external dependencies
    
    v_a = [1.0, 3.5, 4.2]
    v_b = [1.0, 2.9, 8.0]
    
    result = VectorComparator.is_less_than_or_equal(v_a, v_b)
    
    print(f"Comparing {v_a} and {v_b}")
    print(f"Result (lexicographical check stopping at first diff): {result}")

    # Additional test case for equality logic
    v_c = [5.0, 10.0]
    v_d = [5.0, 10.0]
    
    result2 = VectorComparator.is_less_than_or_equal(v_c, v_d)
    print(f"Comparing {v_c} and {v_d}")
    # Note: Based on logic derived (return True if no diff found in common part), this returns True for equality.
    # If the intent was strictly less via difference only, it would be False. 
    # Given "less than or equal", equality is valid.
    
    print(f"Result for identical vectors: {result2}")

    # Test case where first element differs immediately
    v_e = [10.5]
    v_f = [20.0, 30.0]
    
    result3 = VectorComparator.is_less_than_or_equal(v_e, v_f)
    print(f"Comparing {v_e} and {v_f}")
    # First diff: 10.5 < 20.0 -> True
    
    print(f"Result for first element strictly less: {result3}")

    # Test case where first element violates condition immediately
    v_g = [20.0]
    v_h = [10.0, 999.0]
    
    result4 = VectorComparator.is_less_than_or_equal(v_g, v_h)
    print(f"Comparing {v_g} and {v_h}")
    # First diff: 20.0 > 10.0 -> False
    
    print(f"Result for first element strictly greater (fail): {result4}")