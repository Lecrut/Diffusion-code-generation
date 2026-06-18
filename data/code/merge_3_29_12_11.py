class StringReverser:
    def reverse(self, text):
        """
        Reverses a given string efficiently using slicing.
        
        Args:
            text (str): The input string to be reversed.
            
        Returns:
            str: A new string with the characters in reverse order.
        """
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    test_cases = [
        "Hello, World!",
        "",
        "A",
        "Python is great.",
        12345  # Note: This will fail if passed as int due to type mismatch in slicing logic expectation, 
             # but Python allows slicing on ints which returns empty string. We ensure str input for clarity below.
    ]

    print("Testing StringReverser class:")
    
    for test_input in test_cases:
        try:
            if isinstance(test_input, int):
                converted = str(test_input)
                result = StringReverser().reverse(converted)
                print(f"Input (converted to string): {test_input} -> Output: '{result}'")
            else:
                reversed_str = StringReverser().reverse(test_input)
                print(f"Input: \"{test_input}\" -> Output: \"{reversed_str}\"")
        except Exception as e:
            print(f"Error processing input: {e}")