class StringManipulator:
    def swap_all_pairs(self, text):
        """
        Swaps all adjacent character pairs in the input string in-place (conceptually).
        
        Since Python strings are immutable, this method returns a new string with 
        swapped pairs. If there is an odd number of characters, the last one remains unchanged.
        
        Args:
            text (str): The input string to manipulate.
            
        Returns:
            str: A new string with all adjacent character pairs swapped.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        
        # Convert list of characters for mutability during processing logic simulation
        chars = list(text)
        length = len(chars)
        
        # Iterate through the list in steps of 2 and swap adjacent pairs
        for i in range(0, length - 1, 2):
            if i + 1 < length:
                # Swap characters at index i and i+1
                chars[i], chars[i + 1] = chars[i + 1], chars[i]
        
        return ''.join(chars)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    test_cases = [
        "ab",           # Expected: ba
        "abcdef",       # Expected: bacdef -> wait, pairs are (a,b), (c,d) -> b a d c f? 
                       # Let's re-verify logic: indices 0&1 swap, 2&3 swap. 
                       # Input: a(0)b(1)c(2)d(3)e(4)f(5)
                       # Swap 0,1 -> ba; Swap 2,3 -> dc; e,f remain? No f is index 5. Wait length 6.
                       # Indices: 0(a), 1(b), 2(c), 3(d), 4(e), 5(f). 
                       # Pairs: (a,b) -> ba, (c,d) -> dc, (e,f) -> fe. Result: badcf e? No "bad cfe".
        "abcdef",       # Correct trace: a<->b => b,a; c<->d => d,c; e<->f => f,e. Output: "badcfe"
        "abcde",        # Odd length last char stays same. Pairs (a,b)->ba, (c,d)->dc, 'e' stays. Result: "bacde"
        "",             # Empty string returns empty
        "x",            # Single character remains unchanged
    ]

    manipulator = StringManipulator()

    for i, text in enumerate(test_cases):
        result = manipulator.swap_all_pairs(text)
        print(f"Input: '{text}' -> Output: '{result}'")