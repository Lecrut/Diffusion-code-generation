class StringManipulator:
    def swap_all_pairs(self, text):
        """
        Swaps all adjacent character pairs in the input string in-place (logically).
        
        Since Python strings are immutable, this method returns a new list of characters
        representing the swapped sequence. The term 'in-place' is interpreted as modifying
        the underlying data structure efficiently without allocating extra space for intermediate lists 
        beyond what's necessary for the result representation if converted to string later.

        Args:
            text (str): The input string containing even or odd length of characters.
            
        Returns:
            str: A new string with all adjacent character pairs swapped.
        
        Example:
            >>> s = StringManipulator()
            >>> s.swap_all_pairs("ab") -> "ba"
            >>> s.swap_all_pairs("abcd") -> "badc"
            >>> s.swap_all_pairs("abcde") -> "baced" (last char remains)
        """
        # Convert string to list for mutability
        chars = list(text)
        
        # Iterate over the list with a step of 2, swapping elements at indices i and i+1 if both exist
        n = len(chars)
        for i in range(0, n - 1, 2):
            j = i + 1
            chars[i], chars[j] = chars[j], chars[i]
        
        # Join the list back into a string and return it as this is the only efficient way 
        # to create a new mutable-like result from an immutable input in Python efficiently.
        return "".join(chars)

if __name__ == '__main__':
    # Sample test cases running without user interaction or external dependencies
    
    sm = StringManipulator()
    
    # Test case 1: Even length, simple pair swap
    sample_1 = "abcd"
    result_1 = sm.swap_all_pairs(sample_1)
    print(f"Input: '{sample_1}' -> Output: '{result_1}'") 
    assert result_1 == "badc", f"Expected 'badc', got '{result_1}'"

    # Test case 2: Odd length, last character stays put
    sample_2 = "abcdefg"
    result_2 = sm.swap_all_pairs(sample_2)
    print(f"Input: '{sample_2}' -> Output: '{result_2}'") 
    assert result_2 == "bafedcg", f"Expected 'bafedcg', got '{result_2}'"

    # Test case 3: Single character (edge case, no pairs to swap)
    sample_3 = "a"
    result_3 = sm.swap_all_pairs(sample_3)
    print(f"Input: '{sample_3}' -> Output: '{result_3}'") 
    assert result_3 == "a", f"Expected 'a', got '{result_3}'"

    # Test case 4: Two characters (basic swap)
    sample_4 = "xy"
    result_4 = sm.swap_all_pairs(sample_4)
    print(f"Input: '{sample_4}' -> Output: '{result_4}'") 
    assert result_4 == "yx", f"Expected 'yx', got '{result_4}'"

    # Test case 5: Empty string (edge case)
    sample_5 = ""
    result_5 = sm.swap_all_pairs(sample_5)
    print(f"Input: '{sample_5}' -> Output: '{result_5}'") 
    assert result_5 == "", f"Expected '', got '{result_5}'"

    # Test case 6: Larger random-like string with repeating patterns to ensure correctness across multiple pairs
    sample_6 = "1234567890ABCDEF"
    result_6 = sm.swap_all_pairs(sample_6)
    print(f"Input: '{sample_6}' -> Output: '{result_6}'") 
    assert result_6 == "21436587FEDCBA", f"Expected '21436587FEDCBA', got '{result_6}'"

    print("All tests passed successfully.")