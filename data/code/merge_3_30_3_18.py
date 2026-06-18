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
                # Swap current pair and append to result list
                result.append(text[i + 1])
                result.append(text[i])
                i += 2
            else:
                # Handle the last odd character
                result.append(text[i])
                break
        
        return ''.join(result)

if __name__ == '__main__':
    manipulator = StringManipulator()

    test_cases = [
        "ab",           # Expected: ba
        "abcde",        # Expected: bacd e -> bace (last 'e' stays)
        "abcdefg",      # Expected: badf cge -> badfcge? No, pairs are (a,b)->(b,a), (c,d)->(d,c)... 
                       # Input: a b c d e f g
                       # Pairs: ab->ba, cd->dc, ef->fe. Last 'g' stays. Result: badcfeg
        "hello",        # Expected: leolh -> l eh ol h? No. (he)->(eh), (ll)->(ll). 
                       # Input: h e l l o
                       # Pairs: he->eh, ll->ll, o->o. Result: ehllo
        "",             # Empty string
    ]

    for text in test_cases:
        output = manipulator.swap_all_pairs(text)
        print(f"Input: '{text}' -> Output: '{output}'")