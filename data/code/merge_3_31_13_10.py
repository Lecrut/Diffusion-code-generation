class StringChecker:
    def check(self, text):
        """
        Determines if a string is a palindrome ignoring case and non-alphanumeric characters.
        
        Args:
            text (str): The input string to check.
            
        Returns:
            bool: True if the string is a palindrome under the specified rules, False otherwise.
        """
        cleaned_text = ''.join(c.lower() for c in text if c.isalnum())
        return cleaned_text == cleaned_text[::-1]

if __name__ == '__main__':
    checker = StringChecker()

    # Sample test cases with hard-coded values (no user input, files, or network)
    samples = [
        "A man a plan a canal Panama",  # True: ignores case and spaces/punctuation
        "race car",                      # True
        "",                             # True: empty string is palindrome
        "hello",                        # False
        "Was it a car or a cat I saw?",# True (ignoring non-alphanumeric)
    ]

    for sample in samples:
        result = checker.check(sample)
        print(f"Input: '{sample}' -> Is Palindrome: {result}")