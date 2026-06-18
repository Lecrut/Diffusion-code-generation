class StringCapitalizer:
    """A class to capitalize specific parts of a string."""

    def capitalize_words(self, input_string):
        """
        Capitalizes only the first letter of each word in the given input string.

        Args:
            input_string (str): The string to process. Words are separated by whitespace.

        Returns:
            str: A new string with the first character of each word capitalized,
                 preserving original casing for all other characters and spacing.
        
        Examples:
            >>> StringCapitalizer().capitalize_words("hello world")
            'Hello World'
            >>> StringCapitalizer().capitalize_words("python is great")
            'Python Is Great'
            >>> StringCapitalizer().capitalize_words("")
            ''
        """
        if not input_string or not isinstance(input_string, str):
            return ""

        # Split the string into words based on whitespace. This handles multiple spaces correctly.
        words = input_string.split()

        capitalized_words = []
        for word in words:
            if len(word) > 0:
                # Capitalize only the first character, keep the rest as is (lowercase or mixed).
                # Using title() would capitalize all letters after spaces which we don't want.
                # We manually take index[0].upper() + slice[1:] to preserve original casing of remaining chars.
                capitalized_word = word[0].capitalize() + word[1:] if len(word) > 1 else word.capitalize()
            else:
                # Handle empty strings resulting from split (though split without args doesn't produce them usually, safe practice).
                capitalized_words.append("")

        return " ".join(capitalized_words)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality.
    test_cases = [
        ("hello world", "Hello World"),
        ("python is great programming language", "Python Is Great Programming Language"),
        ("  leading spaces here ", "  Leading Spaces Here "),
        ("single word", "Single Word"),
        (""),
        ("no change needed in this sentence.", "No Change Needed In This Sentence."),
    ]

    capitalizer = StringCapitalizer()

    print("Running StringCapitalizer tests...\n")
    
    for i, (input_str, expected) in enumerate(test_cases):
        result = capitalizer.capitalize_words(input_str)
        status = "PASS" if result == expected else f"FAIL (Expected: {expected})"
        print(f"Test Case {i+1}: '{input_str}'")
        print(f"Result:   '{result}'")
        print(status)
        print("-" * 40)