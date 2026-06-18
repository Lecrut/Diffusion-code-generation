class StringReverser:
    """A class that provides methods to manipulate strings."""

    def reverse(self, text):
        """
        Reverses the input string in-place if it is a list of characters,
        or returns a new reversed string if `text` is already a string.
        
        Args:
            text (str | list[str]): The input to be reversed. If a string, 
                                   returns a new reversed string. If a list,
                                   reverses in-place and returns None.
            
        Returns:
            str or None: Reversed string if `text` is a string; otherwise None.
        """
        # Ensure we are working with the correct type based on typical usage expectations for strings
        if isinstance(text, str):
            return text[::-1]
        elif isinstance(text, list) and all(isinstance(c, str) for c in text):
            text.reverse()  # Reverses the list in-place
            return None
        else:
            raise TypeError("Input must be a string or a list of strings.")

if __name__ == '__main__':
    # Sample test cases with hard-coded values to ensure no external input is needed
    sample_strings = [
        "hello",
        "Python programming",
        "",
        "A man a plan a canal Panama"  # Note: spaces are preserved in simple slicing
    ]

    reverser = StringReverser()

    for test_input in sample_strings:
        result = reverser.reverse(test_input)
        print(f"Original: '{test_input}'")
        if isinstance(result, str):
            print(f"Reversed: '{result}'")
        else:
            # If the input was a list (not used here but for completeness in logic), it would be modified in-place
            pass
        
    # Additional test with a list of characters to demonstrate full functionality
    char_list = ['h', 'e', 'l', 'l', 'o']
    result_char = reverser.reverse(char_list)  # Should return None as it modifies in place
    print(f"Original List: {char_list}")
    if result_char is not None and isinstance(result_char, str):
        print(f"Reversed String from list logic (hypothetical conversion): '{result_char}'")
    
    # Demonstrate the string reversal specifically which returns a new string
    sample_str = "Hello World!"
    reversed_sample = reverser.reverse(sample_str)
    print(f"\nOriginal: {sample_str}")
    print(f"Reversed: {reversed_sample}")