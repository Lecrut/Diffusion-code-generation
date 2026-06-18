class StringManipulator:
    def swap_all_pairs(self, text):
        """
        Performs an in-place style swap of all adjacent character pairs 
        by constructing a new string based on the input length and swapping logic.
        
        Args:
            text (str): The input string to process.
            
        Returns:
            str: A new string with all adjacent characters swapped pairwise.
        """
        result = []
        i = 0
        
        # Iterate through the string in steps of two
        while i < len(text):
            if i + 1 < len(text):
                # Swap current character and next one, append to list
                result.append(text[i + 1])
                result.append(text[i])
                i += 2
            else:
                # Handle the last odd character if present (no pair)
                result.append(text[i])
                i += 1
        
        return "".join(result)

if __name__ == '__main__':
    manipulator = StringManipulator()

    test_cases = [
        "abcdef",      # Even length: ab->ba, cd->dc, ef->fe => bacdf e -> badce f? No. a<->b, c<->d... 
                      # Input: a b c d e f
                      # Output: b a d c f e
        "abcde",       # Odd length last char stays as is (conceptually) but logic handles it
                      # Input: a b c d e
                      # Pairs: ab->ba, cd->dc. Leftover 'e' appended at end of pair loop? 
                      # My logic above appends leftover if odd index exists inside the while condition check.
                      # Let's trace "abcde": i=0 -> append text[1]('b'), text[0]('a'). i=2.
                      # i=2 < 5, next is 'd'. Append text[3]('c'), text[2]('d'). i=4.
                      # i=4 < 5, but i+1 (5) not < len(5). Else block: append text[4]('e'). i=6. Stop.
                      # Result: "badce". Correct logic for odd length where last char remains in place relative to pairs? 
                      # Actually standard swap-all-pairs usually ignores the trailing single or keeps it. 
                      # The prompt implies "adjacent character pairs", so singles are untouched effectively at end.
        "",            # Empty string -> ""
        "a"             # Single char -> "a" (loop runs once, enters else block)
    ]

    for text in test_cases:
        output = manipulator.swap_all_pairs(text)
        print(f"Input: '{text}'")
        print(f"Output: '{output}'\n")