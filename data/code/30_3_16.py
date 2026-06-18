class StringManipulator:
    def swap_all_pairs(self, text):
        """
        Swaps all adjacent character pairs in the string in-place (conceptually).
        Since Python strings are immutable, this creates a new list of characters
        modified and then returns it as an immutable string.

        Args:
            text (str): The input string to process.
            
        Returns:
            str: A new string with all adjacent pairs swapped.
        
        Example:
            Input: "ab12cd34" -> Output: "ba21dc43"
            Input: "a1b2c3d4e5f6g7h8i9j0k" -> Output: "a1 b2 c3 d4 e5 f6 g7 h8 i9 j0 k" (with spaces for visualization if needed, but here strict swap)
            Actually strictly swapping adjacent pairs regardless of content.
            
        Note: 'in-place' is not possible with standard strings in Python without creating new objects 
        due to immutability; the operation returns a modified string representing the result 
        as if performed sequentially on character positions 0-1, 2-3, etc.
        """
        # Convert string to list of characters for mutability (simulating in-place logic)
        char_list = list(text)

        # Iterate through the list with a step of 2
        n = len(char_list)
        for i in range(n - 1):
            if i + 1 < n:
                # Swap current character with next one
                char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]

        # Join the list back into a string and return
        return "".join(char_list)

if __name__ == '__main__':
    sm = StringManipulator()

    # Test cases hard-coded as required (no user input, network, or files used)
    
    sample_1 = "ab"
    result_1 = swar_all_pairs(sm, ab)  # Corrected logic for swap: should be "ba" if swapped correctly? Wait my code swaps adjacent pairs.