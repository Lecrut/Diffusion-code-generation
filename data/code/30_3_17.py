class StringManipulator:
    def swap_all_pairs(self, text):
        """
        Performs an in-place style swap of all adjacent character pairs 
        on a string (which is immutable in Python, so returns a new list converted to string).
        
        Args:
            text (str): The input string.
            
        Returns:
            str: A new string with all non-overlapping adjacent characters swapped.
        """
        chars = list(text)
        length = len(chars)
        
        # Iterate through the list in steps of 2 and swap pairs
        for i in range(0, length - 1, 2):
            if i + 1 < length:
                chars[i], chars[i + 1] = chars[i + 1], chars[i]
                
        return "".join(chars)

if __name__ == '__main__':
    # Sample values hard-coded to ensure no user input or file access is needed
    sample_text_1 = "abcd"
    sample_text_2 = "hello world!"
    
    manipulator = StringManipulator()
    
    result_1 = manipulator.swap_all_pairs(sample_text_1)
    print(f"Input: {sample_text_1}")
    print(f"Output: {result_1}\n")
    
    # Additional test case with odd length string to ensure last char remains as is
    sample_text_3 = "python"
    result_2 = manipulator.swap_all_pairs(sample_text_3)
    print(f"Input: {sample_text_3}")
    print(f"Output: {result_2}")