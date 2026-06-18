class StringOperation:
    """A class designed to handle various string operations."""
    
    def is_palindrome(self, text: str) -> bool:
        """
        Checks whether a given string is a palindrome.
        
        This method ignores non-alphanumeric characters and case sensitivity.
        
        Args:
            text (str): The input string to check.
            
        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
        return cleaned_text == cleaned_text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to test the method without user input or files
    
    test_cases = [
        "A man, a plan, a canal: Panama",  # Should be True
        "race car",                        # Should be True
        "hello world!",                    # Should be False
        "Madam",                          # Should be True (ignores case)
        "Not a palindrome",                # Should be False
    ]

    string_ops = StringOperation()

    for test_input in test_cases:
        result = string_ops.is_palindrome(test_input)
        print(f"Input: '{test_input}'")
        print(f"Is Palindrome: {result}\n")