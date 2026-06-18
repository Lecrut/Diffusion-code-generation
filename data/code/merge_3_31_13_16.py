class StringChecker:
    def check(self, text):
        """
        Efficiently determines if the input string is a palindrome.
        
        Handles edge cases like empty strings and mixed casing by 
        normalizing the string to lowercase before checking for symmetry 
        while ignoring spaces (though this implementation considers all characters).
        
        This standard approach includes all alphanumeric, punctuation, and space characters.
        If you specifically wish to ignore non-alphanumeric characters, that logic can be added here.

        Args:
            text (str): The string to check for palindrome property.
            
        Returns:
            bool: True if the normalized string is a palindrome, False otherwise.
        """
        # Normalize case by converting all uppercase letters to lowercase
        normalized_text = text.lower()
        
        # Check if empty or single character (always palindromes)
        n = len(normalized_text)
        if n <= 1:
            return True
        
        left, right = 0, n - 1
        
        while left < right:
            if normalized_text[left] != normalized_text[right]:
                return False
            left += 1
            right -= 1
            
        return True

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    checker = StringChecker()
    
    test_cases = [
        "",                          # Empty string: should be True
        "a",                         # Single character: should be True
        "A man, a plan, a canal: Panama",  # Classic example with spaces and punctuation (case-insensitive)
        "Hello World",               # Not a palindrome due to 'H' != 'd', space mismatch if not ignored
        "madam",                     # Simple lowercase palindrome
        "RaceCar",                   # Mixed case palindrome
    ]
    
    for text in test_cases:
        result = checker.check(text)
        print(f"'{text}' is a palindrome: {result}")