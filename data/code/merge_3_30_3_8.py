class StringManipulator:
    def swap_all_pairs(self, text):
        """
        Swaps all adjacent character pairs in the input string in-place (conceptually).
        
        Since Python strings are immutable, this method returns a new string 
        with swapped pairs. If there is an odd number of characters, the last one remains unchanged.

        Args:
            text (str): The input string to process.

        Returns:
            str: A new string with all adjacent character pairs swapped.
        """
        result = []
        
        # Iterate over the string in steps of 2
        for i in range(0, len(text), 2):
            # Append both characters if a pair exists (i+1 < length)
            if i + 1 < len(text):
                result.append(text[i])
                result.append(text[i + 1])
            else:
                # If the last character is alone, append it as is
                result.append(text[i])
        
        return ''.join(result)

if __name__ == '__main__':
    sm = StringManipulator()

    # Sample test cases with hard-coded values
    sample_1 = "abcdef"
    expected_1 = "bacdef"
    
    sample_2 = "abcd"
    expected_2 = "badc"
    
    sample_3 = "a"  # Odd length string
    expected_3 = "a"

    print(f"Input: '{sample_1}' -> Output: '{sm.swap_all_pairs(sample_1)}' (Expected: '{expected_1}')")
    assert sm.swap_all_pairs(sample_1) == expected_1, f"Test 1 failed. Got {sm.swap_all_pairs(sample_1)}, Expected {expected_1}"

    print(f"Input: '{sample_2}' -> Output: '{sm.swap_all_pairs(sample_2)}' (Expected: '{expected_2}')")
    assert sm.swap_all_pairs(sample_2) == expected_2, f"Test 2 failed. Got {sm.swap_all_pairs(sample_2)}, Expected {expected_2}"

    print(f"Input: '{sample_3}' -> Output: '{sm.swap_all_pairs(sample_3)}' (Expected: '{expected_3}')")
    assert sm.swap_all_pairs(sample_3) == expected_3, f"Test 3 failed. Got {sm.swap_all_pairs(sample_3)}, Expected {expected_3}"

    print("All tests passed.")