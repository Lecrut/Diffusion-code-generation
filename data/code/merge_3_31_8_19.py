class StringOperations:
    """A class designed to perform various string operations."""

    def is_palindrome(self, input_string):
        """
        Checks if a given string is a palindrome, ignoring spaces and case sensitivity.
        
        Args:
            input_string (str): The string to check for palindromic property.
            
        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        cleaned = ''.join(char.lower() for char in input_string if char.isalnum())
        return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "#aB#xZ#YX#",
        "",
        "Madam"
    ]

    string_ops = StringOperations()

    print("Palindrome Check Results:\n")
    for test in test_cases:
        result = string_ops.is_palindrome(test)
        # Using f-string only to format the output, no user interaction involved
        formatted_output = (f'Input: "{test}" -> Is Palindrome: {result}\n')
        print(formatted_output.format())