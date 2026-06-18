class StringChecker:
    def check(self, text):
        """
        Determines if the input string is a palindrome.
        
        Handles edge cases like empty strings and mixed casing by normalizing 
        to lowercase before comparison. Non-alphanumeric characters are ignored 
        (though based on strict 'palindrome' definition in common contexts without 
        specifying filtering, this implementation treats only alphanumeric characters as valid).

        :param text: The input string to check
        :return: True if the normalized alphanumeric sequence is a palindrome, False otherwise
        """
        # Normalize the string: convert to lowercase and keep only alphanumeric characters
        cleaned_text = ''.join(char.lower() for char in text if char.isalnum())

        # Check if empty after cleaning (empty strings are palindromes)
        return cleaned_text == cleaned_text[::-1]

if __name__ == '__main__':
    checker = StringChecker()
    
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        "", 
        ("Was it a car or a cat I saw?", True),
        ("Hello", False),
        ("Madam", True)
    ]

    for test_input, expected in test_cases:
        result = checker.check(test_input)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] Input: '{test_input}' -> Result: {result} (Expected: {expected})")