class StringManipulator:
    def swap_all_pairs(self, text):
        """
        Swaps all adjacent character pairs in the input string in-place (conceptually).
        
        Since Python strings are immutable, this method returns a new string with 
        swapped pairs. If there is an odd number of characters, the last one remains unchanged.
        
        Args:
            text (str): The input string to process.
            
        Returns:
            str: A new string with all adjacent character pairs swapped.
        """
        result = []
        i = 0
        
        while i < len(text):
            if i + 1 < len(text):
                # Swap the pair and append both characters in reversed order
                result.append(text[i+1])
                result.append(text[i])
                i += 2
            else:
                # Handle odd-length string by appending the last character as is
                result.append(text[i])
                break
                
        return ''.join(result)

if __name__ == '__main__':
    manipulator = StringManipulator()

    # Sample test cases with hard-coded values
    sample1 = "abcd"
    expected1 = "badc"
    
    sample2 = "abcdefg"
    expected2 = "bafcdge"
    
    sample3 = "a"
    expected3 = "a"

    # Run tests and print results
    assert manipulator.swap_all_pairs(sample1) == expected1, f"Test 1 failed: {manipulator.swap_all_pairs(sample1)} != {expected1}"
    assert manipulator.swap_all_pairs(sample2) == expected2, f"Test 2 failed: {manipulator.swap_all_pairs(sample2)} != {expected2}"
    assert manipulator.swap_all_pairs(sample3) == expected3, f"Test 3 failed: {manipulator.swap_all_pairs(sample3)} != {expected3}"

    print("All tests passed.")
    
    # Demonstration of the function with sample inputs
    demo_text = "1234567890"
    swapped_result = manipulator.swap_all_pairs(demo_text)
    print(f"Original: '{demo_text}'")
    print(f"Swapped : '{swapped_result}'")