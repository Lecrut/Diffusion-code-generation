class StringOperations:
    """A class designed to perform various string operations."""

    def is_palindrome(self, text: str) -> bool:
        """
        Checks if a given string is a palindrome.
        
        A palindrome is a word, phrase, number, or other sequence of characters 
        which reads the same backward as forward, ignoring spaces and case sensitivity.
        
        Args:
            text (str): The input string to check.
            
        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        # Normalize the string by converting to lowercase and removing non-alphanumeric characters for robustness
        normalized_text = ''.join(char.lower() for char in text if char.isalnum())
        
        return normalized_text == normalized_text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to test the method without user input or external dependencies
    
    # Test cases with expected results: True, False, True, False
    samples = [
        "A man a plan a canal Panama",  # Should be True (ignoring spaces and case)
        "race car",                     # Should be True
        "hello world",                  # Should be False
        "Madam",                       # Should be True
        "1234567890",                  # Should be False
    ]

    string_ops = StringOperations()

    for sample in samples:
        result = string_ops.is_palindrome(sample)
        print(f"Input: '{sample}' -> Is Palindrome: {result}")