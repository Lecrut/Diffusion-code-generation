class StringReverser:
    def reverse(self, word):
        """
        Reverses a single input string character by character without modifying arguments passed by reference (since Python strings are immutable).
        
        Args:
            word (str): The string to be reversed.
            
        Returns:
            str: A new string containing the characters of 'word' in reverse order.
        """
        return ''.join(word[::-1])

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        "hello",
        "",
        "A man a plan, a canal: Panama!",
    ]

    reverser = StringReverser()

    print("String Reversal Results:")
    print("-" * 30)
    
    for word in test_cases:
        reversed_word = reverser.reverse(word)
        original_length = len(word)
        result_length = len(reversed_word)
        
        print(f"Original input length: {original_length}")
        print(f"Reversed string length: {result_length}")
        print(f"\nInput String  : \"{word}\"")