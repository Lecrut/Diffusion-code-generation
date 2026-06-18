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
        
        Example:
            >>> manipulator = StringManipulator()
            >>> result = manipulator.swap_all_pairs("ab")
            >>> print(result)  # Output: 'ba'
            
            >>> result = manipulator.swap_all_pairs("abcd")
            >>> print(result)  # Output: 'bacd' -> Wait, logic check: ab->ba cd->dc => bacd? No. 
            Correction on example above: "ab" becomes "ba", "cd" becomes "dc". So "abcd" becomes "badc".
        """
        chars = list(text)
        
        # Iterate through the string in steps of 2
        for i in range(0, len(chars), 2):
            if i + 1 < len(chars):
                # Swap characters at index i and i+1
                chars[i], chars[i + 1] = chars[i + 1], chars[i]
        
        return ''.join(chars)

if __name__ == '__main__':
    manipulator = StringManipulator()

    sample_inputs = [
        "ab",           # Expected: ba
        "abcd",         # Expected: badc (a<->b, c<->d)
        "abcdefg",      # Expected: bacdefg (e remains last as odd index 6 is even? indices 0-1 swap, 2-3 swap. f at 5 swaps with g at 4? Wait. 
                       # Indices: a(0), b(1), c(2), d(3), e(4), f(5), g(6)
                       # Swap (0,1): ba...; Swap (2,3): ...dc...; Swap (4,5): ...fed? No. 
                       # Let's trace carefully:
                       # Input: a b c d e f g
                       # Pairs: (a,b), (c,d), (e,f) -> last char 'g' left alone.
                       # Swapped: b a d c f e g
        "hello",       # Expected: ehllh? h(0)e(1)->eh, l(2)o(3)->ol, o(4)? No wait. 
                       # Indices: h(0), e(1), l(2), l(3), o(4)
                       # Swap (0,1): eh...; Swap (2,3): ...lo -> ol? Yes. Last 'o' stays. Result: eholo.
        "a"             # Expected: a (no pairs)
    ]

    for text in sample_inputs:
        result = manipulator.swap_all_pairs(text)
        print(f"'{text}' -> '{result}'")