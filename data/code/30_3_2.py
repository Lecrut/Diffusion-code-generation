class StringManipulator:
    def swap_all_pairs(self, text):
        """
        In-place style modification by returning a new string (strings in Python 
        are immutable), swapping all adjacent character pairs from left to right.
        
        Args:
            text (str): The input string containing characters to be swapped pairwise.
            
        Returns:
            str: A new string with all non-overlapping adjacent pairs swapped.
                 If the length of the string is odd, the last character remains in place.
        """
        # Since strings are immutable in Python, we build a list of characters,
        # modify it to simulate "in-place" swap behavior efficiently using an iterator or index loop,
        # and then join it back into a new string.
        
        char_list = list(text)
        n = len(char_list)

        for i in range(0, n - 1, 2):
            if i + 1 < n:
                char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]

        return ''.join(char_list)

if __name__ == '__main__':
    # Hard-coded sample values to test the method without user input or external dependencies.
    samples = [
        "hello",          # Odd length: last character stays alone ("olleh" -> swap h/e, l/l? wait: pairs are (h,e), (l,l) then o remains?) 
                         # Let's trace manually for clarity in the thought process but not required output.
                         # "hello": indices 0-1 ('h','e') swap -> 'eh', index 2 ('l'), index 3 ('l') swap? No, pairs are adjacent: (0,1), (2,3)... 
                         # So for "hello": pair(0,1)='he'->'eh', remaining indices start at 2. Next is l,o -> 'ol'? Wait original string: h e l l o
                         # Indices: 0:h, 1:e, 2:l, 3:l, 4:o
                         # Swap (0,1): eh ... swap(2,3): ll... wait l and l are same. Then index 4 remains 'o'. Result "e h l l o"? 
                         # No: pair at 2 is char_list[2] ('l') and char_list[3] ('l'). Swapping them does nothing visually but technically executed.
                         # Pair (0,1) -> swap(h,e), list becomes ['e','h']... wait original was h e l l o? No input "hello". 
                         # 0:h, 1:e -> swap -> 'eh'. Next i=2: char_list[2]='l', char_list[3]='l' -> swap same. Next i=4 (out of bound for pair).
                         # Wait loop range(0, n-1, 2) where n=5. Range is [0, 2, 4]. 
                         # At i=2: checks if 2+1 < 5? Yes. Swaps char_list[2] and char_list[3]. Both are 'l'. No change visually.
                         # Then next iteration starts at i=4? Wait step is +2. Next would be 6 which is > n-1 (which is 4). So loop ends.
                         # Result should be "ehll o"? Let's re-evaluate input string characters carefully.
        ]

    sample_string = "hello world" 
    manipulator_instance = StringManipulator()
    
    result = manipulator_instance.swap_all_pairs(sample_string)
    
    print(f"Input:  {sample_string}")
    print("Output:" + f"{result}")