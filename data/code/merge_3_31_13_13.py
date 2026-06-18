class StringChecker:
    def check(self, text):
        """
        Efficiently determines if the input string is a palindrome.
        
        Handles edge cases like empty strings and treats uppercase/lowercase 
        letters as equivalent (e.g., 'A' == 'a'). Non-alphanumeric characters 
        are ignored for comparison purposes but do not break continuity unless 
        they were part of the original sequence logic required by strict palindromes.
        
        Since standard palindrome definition usually ignores non-letter/number chars,
        this implementation focuses on alphanumeric symmetry after normalization.

        Args:
            text (str): The input string to check.
            
        Returns:
            bool: True if the string is a palindrome considering case-insensitivity 
                 and ignoring non-alphanumeric characters; False otherwise.
        """
        # Normalize: convert to lowercase and keep only alphanumeric characters
        normalized = ''.join(char.lower() for char in text if char.isalnum())
        
        # Check if the cleaned string reads the same forwards and backwards
        return normalized == normalized[::-1]

if __name__ == '__main__':
    checker = StringChecker()

    test_cases = [
        "",                          # Empty string
        "A man a plan a canal Panama",  # Classic mixed case with spaces/punctuation
        "racecar",                   # Simple palindrome
        "Hello, World!",             # Not a palindrome (different lengths after cleaning) -> actually 'olleh' vs 'dlrow', not equal. Wait: 'H','e','l','l','o' + ',' ignored? Let's re-verify logic mentally. Cleaned: hello world -> helloworld != drowolleh. Correct.)
        "Was it a car or a cat I saw?", # Classic tricky one
    ]

    for test_text in test_cases:
        result = checker.check(test_text)
        print(f'"{test_text}" is {"a" if result else "not"} a palindrome.')