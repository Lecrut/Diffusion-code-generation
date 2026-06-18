import math

class VectorComparator:
    @staticmethod
    def compare_less_equal(v1, v2):
        """
        Compares two vectors element-wise up to the first differing index.
        Returns True if all elements in v1 seen so far are <= corresponding 
        elements in v2 at those indices, and for the first pair where they differ, 
        v1[i] < v2[i]. If no differences exist (v1 == v2), it returns False unless 
        we consider strict inequality on the 'first differing' logic which implies a difference must occur.
        
        However, re-reading "element-wise less than or equal to ... considering only the first differing element":
        This phrasing suggests that if there is a difference, the comparison stops and checks condition at that index.
        If no difference exists throughout the length of shorter list? 
        Let's interpret strictly: Find the smallest index 'i' where v1[i] != v2[i].
        - If such i exists: return True ONLY IF v1[i] <= v2[i]? No, usually "less than" implies strict.
          The prompt says "element-wise less than or equal to... considering only the first differing element".
          This is slightly ambiguous. 
          Interpretation A: Is v1[k] < v2[k] for all k where they differ? And return False if any are >? 
          But it restricts consideration TO THE FIRST DIFFERING ELEMENT.
          
          Most logical interpretation for "considering only the first differing element":
          We scan from start to find index 'i' such that v1[i] != v2[i].
          If found, we return True if and only if (condition based on i). 
          The prompt says "element-wise less than or equal". Usually <= means a_i <= b_a.
          But the constraint is "considering ONLY the first differing element".
          This implies: Check v1[i] vs v2[i]. If they are different, does that specific relation hold?
          Actually, standard lexicographical comparison stops at the first difference to break ties for order.
          
          Let's assume the logic: 
          Iterate through indices i = 0..min_len-1.
          Find first index where v1[i] != v2[i].
          If found (diff exists): return True if v1[i] < v2[i]? Or <=?
          Prompt says "less than or equal to". So condition is likely v1[i] <= v2[i]. 
          Since they differ, strict inequality must hold. i.e., v1[i] < v2[i].
          
          If NO difference found in the valid range (all compared elements were equal):
          In standard lexicographical comparison "list1 <= list2", if lists are identical up to length of shorter, 
          we check lengths. But here it says "considering only first differing". 
          This implies if no difference exists, maybe return False or treat as undefined? 
          Given the specificity of "first differing element", likely a mismatch must exist for this specific constraint logic 
          to apply meaningfully in isolation from full lexicographical rules.
          
          Revised Logic:
          1. Find first index i where v1[i] != v2[i]. Stop at min(len(v1), len(v2)).
          2. If such an index exists: Return True if v1[i] <= v2[i] (which effectively means < since they differ). Else False.
          3. If NO difference exists within the bounds of shorter list: 
             This case is tricky with "considering only first differing". 
             Perhaps return False because no condition was met? Or maybe treat as True if all elements are equal?
             Let's assume strict behavior required by the phrasing implies a discrepancy check. 
             If vectors are identical, there is NO first differing element. Thus the condition cannot be evaluated or fails vacuously/falsely depending on context.
             For safety in code generation: Return False if no difference found (as per "first differing" requirement not met).

        :param v1: List of numbers.
        :param v2: List of numbers.
        :return: Boolean result of comparison based on first differing element logic.
        """
        min_len = len(v1) if len(v1) < len(v2) else len(v2)

        for i in range(min_len):
            # If elements are different, this is our target index
            if v1[i] != v2[i]:
                # "element-wise less than or equal to" -> v1[i] <= v2[i]
                # Since they differ strictly (< >), we check < 
                return v1[i] <= v2[i]

        # No differing element found up to min length.
        # As per constraint of checking ONLY the first differing, none exists.
        # Returning False as a safe default for "did it satisfy X considering only Y" where Y didn't happen.
        return False

if __name__ == '__main__':
    # Sample test cases run directly without input
    tc1 = [1, 2]
    tc2 = [3, 4]
    print(compare_less_equal(tc1, tc2))  # True (1<3)

    vc = VectorComparator()
    
    res1 = vc.compare_less_equal([5], [6])      # True (5 < 6)
    assert res1 is True
    
    res2 = vc.compare_less_equal([7], [4])       # False (7 > 4)
    assert res2 is False
    
    res3 = vc.compare_less_equal([1, 1], [1, 2]) # Index 0: 1==1. Index 1 differs? 
        # Wait loop continues to index 1. v1[1]=1, v2[1]=2. Differs. 1<=2 is True.
    res3_expected = vc.compare_less_equal([1], [1]) # No diff in range (min len=1). Returns False per logic above.
    
    print(res1)
    print(res2)
    print(vc.compare_less_equal([1, 5], [1, 6])) # True at index 1
    
    res4 = vc.compare_less_equal([-10], [-5])     # True (-10 < -5)
    assert res4 is True

    res5 = vc.compare_less_equal([-2], [-9])       # False (-2 > -9)
    assert res5 is False

    print("All sample tests passed.")