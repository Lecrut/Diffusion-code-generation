class StringManipulator:
    def swap_all_pairs(self, text):
        """
        Swaps all adjacent character pairs in the input string in-place (conceptually).
        
        Since Python strings are immutable, this method returns a new string 
        where every pair of characters has been swapped. If there is an odd number 
        of characters, the last one remains unchanged.
        
        Args:
            text (str): The input string to process.
            
        Returns:
            str: A new string with all adjacent pairs swapped.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")

        result = []
        for i in range(0, len(text), 2):
            # Append the second character of the pair first (if it exists)
            if i + 1 < len(text):
                result.append(text[i + 1])
            # Then append the first character of the pair
            result.append(text[i])

        return ''.join(result)

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or external dependencies
    
    samples = [
        "hello",           # Odd length: 'eh' -> 'he', 'll' -> 'lh', 'o' stays
        "abcdefg",         # Even length: ab->ba, cd->dc, ef->fe, g stays? No wait. 
                          # Pairs are (a,b), (c,d), (e,f). Result should be b a d c f e ... but logic swaps adjacent pairs.
                          # Input "abcdefg": indices 0-1 ('ab') -> 'ba', 2-3 ('cd') -> 'dc', 4-5 ('ef') -> 'fe'. Index 6 is single.
        "aabbcc",          # Even length, perfect pairing
        "",                # Empty string edge case
    ]

    manipulator = StringManipulator()

    for sample in samples:
        swapped_text = manipulator.swap_all_pairs(sample)
        print(f"Original: '{sample}' -> Swapped: '{swapped_text}'")