class StringOperations:
    """A class designed to perform various string operations."""

    def is_palindrome(self, text: str) -> bool:
        """
        Checks if a given string is a palindrome.
        
        A palindrome is a word, phrase, number, or other sequence of 
        characters that reads the same forward and backward (ignoring spaces).
        
        Args:
            text (str): The input string to check.
            
        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        cleaned_text = ''.join(char.lower() for char in text)
        return cleaned_text == cleaned_text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to test the method without user input
    
    test_cases = [
        "A man a plan a canal Panama",
        "race car",
        "hello world",
        "Madam",
        "",
        "12321"
    ]

    string_ops = StringOperations()

    for text in test_cases:
        result = string_ops.is_palindrome(text)
        print(f"'{text}' is {'a' if result else 'not a'} palindrome.")