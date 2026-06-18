class StringOperations:
    """A class designed to perform various string operations."""

    @staticmethod
    def is_palindrome(text: str) -> bool:
        """
        Check if a given string is a palindrome, ignoring case and non-alphanumeric characters.

        Args:
            text (str): The input string to check.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
        return cleaned_text == cleaned_text[::-1]

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race car",
        "hello world",
        "Was it a car or a cat I saw?",
        "",
        "Madam"
    ]

    string_ops = StringOperations()

    for test_input in test_cases:
        result = string_ops.is_palindrome(test_input)
        print(f"'{test_input}' is {'a' if result else 'not'} a palindrome.")