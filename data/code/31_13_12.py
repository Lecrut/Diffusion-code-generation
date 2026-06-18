import re

class StringChecker:
    def check(self, text):
        """
        Efficiently determines if the input string is a palindrome.
        
        Handles edge cases like empty strings and mixed casing by converting 
        to lowercase and removing non-alphanumeric characters before comparison.
        
        Args:
            text (str): The input string to check.
            
        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        # Convert to lowercase and keep only alphanumeric characters for efficiency
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
        
        # Use two-pointer approach or slicing (slicing is efficient in Python)
        return cleaned_text == cleaned_text[::-1]

if __name__ == '__main__':
    checker = StringChecker()
    
    sample_cases = [
        "",                     # Empty string
        "A man a plan a canal Panama",  # Classic palindrome with spaces and punctuation
        "No 'x' in Nixon",      # Mixed casing and quotes
        "Hello, World!",       # Not a palindrome
        "Was it a car or a cat I saw?",  # Another classic example
    ]
    
    for text in sample_cases:
        result = checker.check(text)
        print(f"Input: '{text}' -> Is Palindrome: {result}")