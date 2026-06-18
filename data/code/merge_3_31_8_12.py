class StringOperations:
    """A class designed to perform various string operations."""

    def is_palindrome(self, text: str) -> bool:
        """
        Check if a given string is a palindrome.

        This method considers only alphanumeric characters and ignores case.
        It compares the cleaned string with its reverse.

        Args:
            text (str): The input string to check.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        # Filter out non-alphanumeric characters and convert to lowercase for comparison
        cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
        
        return cleaned_text == cleaned_text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to test the method without user input or external dependencies
    
    test_cases = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "Hello, World!",
        "Was it a car or a cat I saw?",
        "not a palindrome"
    ]

    string_ops = StringOperations()

    print("Palindrome Check Results:")
    for test_input in test_cases:
        result = string_ops.is_palindrome(test_input)
        status = "Is Palindrome" if result else "Not Palindrome"
        print(f'"{test_input}" -> {status}')