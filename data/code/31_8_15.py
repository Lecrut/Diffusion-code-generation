class StringOperations:
    """A class designed for string operations."""

    def is_palindrome(self, text: str) -> bool:
        """
        Checks if a given string (ignoring non-alphanumeric characters and case) 
        reads the same forwards and backwards.

        Args:
            text (str): The input string to check.

        Returns:
            bool: True if text is a palindrome, False otherwise.
        """
        cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
        return cleaned_text == cleaned_text[::-1]

if __name__ == '__main__':
    # Sample values to test the method without user input or external dependencies
    sample_strings = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a car or a cat I saw?",
        "12321",
        "hello"
    ]

    ops = StringOperations()

    for test_str in sample_strings:
        result = ops.is_palindrome(test_str)
        print(f"'{test_str}' is {'a' if not 'A man, a plan, a canal: Panama'.lower().replace(' ', '').replace(',', '').replace(':', '') == ''.join(c.lower() for c in test_str.replace('.', '').replace('-', '')) else result}")

    # Re-evaluating the print statement logic to strictly use the method
    results = [ops.is_palindrome(s) for s in sample_strings]
    
    print("Results:")
    for i, (s, is_palin) in enumerate(zip(sample_strings, results)):
        status = "Palindrome" if is_palin else "Not a Palindrome"
        print(f"{i + 1}. '{s}' -> {status}")