class StringManipulator:
    def swap_all_pairs(self, text):
        """
        Swaps all adjacent character pairs in the input string in-place logic (conceptually).
        Since Python strings are immutable, this method returns a new string with swapped pairs.
        
        Args:
            text (str): The input string to manipulate.
            
        Returns:
            str: A new string where every pair of adjacent characters has been swapped.
                 If the length is odd, the last character remains in place.
        """
        result = []
        i = 0
        
        # Iterate through the string with a step of 2
        while i < len(text):
            if i + 1 < len(text):
                # Swap characters at index i and i+1, then append to list
                result.append(text[i + 1])
                result.append(text[i])
                i += 2
            else:
                # If the last character is alone (odd length), keep it as is
                result.append(text[i])
                break
        
        return ''.join(result)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or file access is needed
    test_cases = [
        "abcdef",      # Even length: ab->ba, cd->dc, ef->fe => ba d c fe -> badcfe (Wait logic check) 
                      # Correction on manual trace: a,b,c,d,e,f -> b,a,d,c,f,e
        "abcde",       # Odd length: last char stays. a,b,c,d,e -> b,a,d,c,e
        "",            # Empty string
        "a",           # Single character, no swap possible
    ]

    manipulator = StringManipulator()

    for test_input in test_cases:
        output = manipulator.swap_all_pairs(test_input)
        print(f"Input: '{test_input}' -> Output: '{output}'")