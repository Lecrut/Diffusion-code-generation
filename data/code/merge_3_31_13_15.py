class StringChecker:
    def check(self, text):
        """
        Determines if the input string is a palindrome.
        
        Handles edge cases such as empty strings and mixed casing by converting
        to lowercase before comparison. Non-alphanumeric characters are ignored 
        for the purpose of this implementation (only letters and digits count).

        Args:
            text (str): The input string to check.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        # Filter out non-alphanumeric characters and convert to lowercase
        cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
        
        # Check if the cleaned string reads the same forwards and backwards
        return cleaned_text == cleaned_text[::-1]

if __name__ == '__main__':
    checker = StringChecker()

    # Hard-coded sample values to test various cases including empty strings, 
    # mixed casing, special characters, numbers, etc.
    samples = [
        "",                          # Empty string (should be True)
        "A man a plan a canal Panama",  # Classic palindrome with spaces and punctuation
        "No 'x' in Nixon",           # Palindrome ignoring non-alphanumeric chars
        "Hello World!",              # Not a palindrome
        "12321",                     # Numeric palindrome
        "Was it a car or a cat I saw?", # Another classic example
    ]

    for sample in samples:
        result = checker.check(sample)
        print(f"Input: '{sample}' -> Is Palindrome: {result}")