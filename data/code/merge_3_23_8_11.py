import sys

class VectorComparator:
    @staticmethod
    def is_less_equal_first_diff(v1, v2):
        """
        Compares two vectors (lists of numbers) element-wise.
        
        Returns True if the first differing element in v1 is less than 
        or equal to the corresponding element in v2; otherwise False.
        If no difference exists up to min(len(v1), len(v2)), returns False.
        """
        # Ensure we don't go out of bounds for either list during iteration
        limit = min(len(v1), len(v2))
        
        for i in range(limit):
            if v1[i] != v2[i]:
                return v1[i] <= v2[i]
            
        # If all compared elements are equal, the condition "first differing element" 
        # has not been met within the common length. Based on strict interpretation:
        # no difference found -> False (as per requirement to consider only first diff)
        return False

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    test_cases = [
        ([1, 2], [3, 4]),       # First diff: 1 < 3 -> True
        ([5, 6], [5, 7]),       # First diff at index 1: 6 > 7 is False (wait, 6<7 so True) 
                                # Correction logic check below in execution
        
        ([4, 2], [4, 3]),       # Equal first, second differs: 2 < 3 -> True
        ([5, 5], [5, 5]),       # No difference found within common length -> False (per spec)
        
        ([10], []),             # v1 longer than v2? Spec says "first differing element". 
                                # If one runs out before diff, no diff exists in common part.
                                
    ]

    results = []
    
    for i, (v1, v2) in enumerate(test_cases):
        res = VectorComparator.is_less_equal_first_diff(v1, v2)
        results.append(f"Test {i+1}: V1={v1}, V2={v2} -> Result: {res}")

    # Print results directly to stdout without prompts or arguments
    for r in results:
        print(r)