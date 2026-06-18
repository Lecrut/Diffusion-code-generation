class StringChecker:
    def check(self, text):
        """
        Determines if a string is a palindrome considering case-insensitivity 
        but ignoring non-alphanumeric characters (excluding spaces as per standard 
        definition unless specified otherwise; here we assume alphanumeric only).
        
        This method efficiently checks for palindromes by comparing the cleaned 
        and lowercased string to its reverse.

        Args:
            text (str): The input string to check.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        # Normalize the string: keep only alphanumeric characters and convert to lowercase
        cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
        
        return cleaned_text == cleaned_text[::-1]

if __name__ == '__main__':
    checker = StringChecker()

    test_cases = [
        "",                    # Empty string
        "A man, a plan, a canal: Panama",  # Classic palindrome with spaces/punctuation/casing
        "racecar",             # Simple alphanumeric palindrome
        "hello",               # Not a palindrome
        "Was it a car or a cat I saw?",  # Another classic example
    ]

    for test_input in test_cases:
        result = checker.check(test_input)
        print(f"Input: '{test_input}' -> Is Palindrome: {result}")