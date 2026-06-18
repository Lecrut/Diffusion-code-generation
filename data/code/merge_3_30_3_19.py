class StringManipulator:
    def swap_all_pairs(self, text):
        """
        Swaps all adjacent character pairs in the input string in-place (conceptually).
        Since Python strings are immutable, this method returns a new string with swapped pairs.
        
        Args:
            text (str): The input string to process.
            
        Returns:
            str: A new string where every pair of characters has been swapped.
                 If the length is odd, the last character remains in place.
        """
        result = []
        i = 0
        
        # Iterate through the string with a step of 2
        while i < len(text):
            if i + 1 < len(text):
                # Swap characters at current index and next index
                result.append(text[i + 1])
                result.append(text[i])
                i += 2
            else:
                # If the last character is alone, append it as is
                result.append(text[i])
                break
        
        return ''.join(result)

if __name__ == '__main__':
    manipulator = StringManipulator()

    sample_1 = "abcdef"
    expected_1 = "bacdef"
    
    sample_2 = "abcd"
    expected_2 = "badc"
    
    sample_3 = "a"
    expected_3 = "a"
    
    sample_4 = "abcde"
    expected_4 = "baced"

    print(f"Input: '{sample_1}' -> Output: '{manipulator.swap_all_pairs(sample_1)}' (Expected: {expected_1})")
    assert manipulator.swap_all_pairs(sample_1) == expected_1, f"Test 1 failed. Got {manipulator.swap_all_pairs(sample_1)}, Expected {expected_1}"

    print(f"Input: '{sample_2}' -> Output: '{manipulator.swap_all_pairs(sample_2)}' (Expected: {expected_2})")
    assert manipulator.swap_all_pairs(sample_2) == expected_2, f"Test 2 failed. Got {manipulator.swap_all_pairs(sample_2)}, Expected {expected_2}"

    print(f"Input: '{sample_3}' -> Output: '{manipulator.swap_all_pairs(sample_3)}' (Expected: {expected_3})")
    assert manipulator.swap_all_pairs(sample_3) == expected_3, f"Test 3 failed. Got {manipulator.swap_all_pairs(sample_3)}, Expected {expected_3}"

    print(f"Input: '{sample_4}' -> Output: '{manipulator.swap_all_pairs(sample_4)}' (Expected: {expected_4})")
    assert manipulator.swap_all_pairs(sample_4) == expected_4, f"Test 4 failed. Got {manipulator.swap_all_pairs(sample_4)}, Expected {expected_4}"

    print("All tests passed.")