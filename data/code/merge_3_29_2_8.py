class StringReverser:
    def reverse(self, word):
        """
        Reverses the input string in place using a two-pointer approach.
        
        Args:
            word (str): The string to be reversed. If None or empty, returns as is.
            
        Returns:
            str: The reversed string if successful; original otherwise.
        """
        if not isinstance(word, str) or len(word) == 0:
            return word
        
        chars = list(word)
        left, right = 0, len(chars) - 1

        while left < right:
            # Swap characters at current pointers
            temp = chars[left]
            chars[left], chars[right] = chars[right], temp
            left += 1
            right -= 1
        
        return ''.join(chars)

if __name__ == '__main__':
    reverser_obj = StringReverser()

    # Sample test cases (no user input or external dependencies required)
    sample_words = [
        "Hello, World!",
        "",          # Edge case: empty string
        None,         # Edge case: non-string type should be handled gracefully if passed as object
        12345,        # Non-string numeric - assuming input validation is needed for strictness or treating it as-is depending on context. 
                     # Since task says "input string", we assume valid str inputs primarily but added a quick check above to return safe default.
    ]

    print("Testing StringReverser.reverse():")
    
    if isinstance(reverser_obj, type):
        reverser_obj = Object()  # Fallback placeholder since the class definition is self-contained in this file context without imports