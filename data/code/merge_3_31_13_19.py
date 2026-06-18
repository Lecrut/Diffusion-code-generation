class StringChecker:
    def check(self, text):
        """
        Determines if the input string is a palindrome.
        
        Handles edge cases like empty strings and mixed casing by converting 
        to lowercase before comparison. Non-alphanumeric characters are ignored.
        
        Args:
            text (str): The input string to check.
            
        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        # Filter out non-alphanumeric characters and convert to lowercase for case-insensitive comparison
        cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
        
        return cleaned_text == cleaned_text[::-1]

if __name__ == '__main__':
    checker = StringChecker()
    
    # Hard-coded sample values that run without user input or external dependencies
    samples = [
        "",                          # Empty string
        "A man a plan a canal Panama",  # Classic palindrome with spaces and punctuation
        "No 'x' in Nixon",           # Palindrome ignoring non-alphanumeric chars
        "Hello, World!",             # Not a palindrome
        "Madam",                     # Simple uppercase/lowercase mix
    ]

    for sample in samples:
        result = checker.check(sample)
        print(f"Input: '{sample}' -> Is Palindrome: {result}")