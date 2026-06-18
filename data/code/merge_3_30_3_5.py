class StringManipulator:
    def swap_all_pairs(self, text):
        """
        Swaps all adjacent character pairs in the input string in-place (conceptually).
        Since strings are immutable in Python, this method returns a new string with swapped pairs.
        
        Args:
            text (str): The input string to process.
            
        Returns:
            str: A new string where every pair of adjacent characters has been swapped.
                 If the length is odd, the last character remains unchanged.
        """
        result = []
        i = 0
        
        # Iterate through the string in steps of 2
        while i < len(text):
            if i + 1 < len(text):
                # Swap characters at index i and i+1
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

    sample1 = "abcd"
    expected1 = "badc"
    
    sample2 = "abcde"
    expected2 = "bacd e"  # 'e' remains at the end
    
    sample3 = ""
    expected3 = ""
    
    sample4 = "a"
    expected4 = "a"

    print("Test Case 1:", manipulator.swap_all_pairs(sample1))
    assert manipulator.swap_all_pairs(sample1) == expected1, f"Expected {expected1}, got {manipulator.swap_all_pairs(sample1)}"

    print("Test Case 2:", manipulator.swap_all_pairs(sample2))
    assert manipulator.swap_all_pairs(sample2) == expected2, f"Expected '{expected2}', got '{manipulator.swap_all_pairs(sample2)}'"

    print("Test Case 3:", repr(manipulator.swap_all_pairs(sample3)))
    assert manipulator.swap_all_pairs(sample3) == expected3, "Empty string test failed"

    print("Test Case 4:", manipulator.swap_all_pairs(sample4))
    assert manipulator.swap_all_pairs(sample4) == expected4, f"Expected '{expected4}', got {manipulator.swap_all_pairs(sample4)}"

    # Additional complex case: even length with multiple pairs
    sample5 = "1234567890"
    result5 = manipulator.swap_all_pairs(sample5)
    print("Test Case 5:", result5)
    assert result5 == "2143658790", f"Expected '2143658790', got '{result5}'"

    # Additional complex case: odd length with multiple pairs
    sample6 = "hello world!"
    result6 = manipulator.swap_all_pairs(sample6)
    print("Test Case 6:", result6)
    assert result6 == "ollehldrowl!", f"Expected 'ollehldrowl!', got '{result6}'"

    print("All tests passed.")